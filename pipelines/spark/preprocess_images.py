from __future__ import annotations

import argparse
import json
from pathlib import Path

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T


def build_spark_session() -> SparkSession:
    return (
        SparkSession.builder.master("local[*]")
        .appName("industrial-ai-platform-preprocess")
        .getOrCreate()
    )


def build_image_metadata_df(spark: SparkSession, image_dir: Path, split_name: str) -> DataFrame:
    image_files = sorted(path for path in image_dir.glob("*.jpg"))
    rows = [
        (
            path.name,
            str(path.resolve()),
            split_name,
        )
        for path in image_files
    ]

    schema = T.StructType(
        [
            T.StructField("image_id", T.StringType(), False),
            T.StructField("image_path", T.StringType(), False),
            T.StructField("dataset_split", T.StringType(), False),
        ]
    )
    return spark.createDataFrame(rows, schema=schema)


def build_annotation_df(spark: SparkSession, train_csv_path: Path) -> DataFrame:
    annotations = spark.read.csv(str(train_csv_path), header=True, inferSchema=True)

    return (
        annotations.groupBy("ImageId")
        .agg(
            F.collect_set("ClassId").alias("annotated_classes"),
            F.count("*").alias("annotation_count"),
            F.sum(F.length("EncodedPixels")).alias("encoded_pixels_char_count"),
        )
        .withColumnRenamed("ImageId", "image_id")
        .withColumn("has_annotation", F.lit(True))
    )


def enrich_with_dimensions(df: DataFrame) -> DataFrame:
    image_schema = T.StructType(
        [
            T.StructField("width", T.IntegerType(), False),
            T.StructField("height", T.IntegerType(), False),
            T.StructField("file_size_bytes", T.LongType(), False),
        ]
    )

    @F.udf(returnType=image_schema)
    def extract_image_metadata(image_path: str) -> tuple[int, int, int]:
        from pathlib import Path

        from PIL import Image

        path = Path(image_path)
        with Image.open(path) as image:
            width, height = image.size
        return width, height, path.stat().st_size

    metadata = extract_image_metadata(F.col("image_path"))
    return (
        df.withColumn("image_metadata", metadata)
        .withColumn("width", F.col("image_metadata.width"))
        .withColumn("height", F.col("image_metadata.height"))
        .withColumn("file_size_bytes", F.col("image_metadata.file_size_bytes"))
        .drop("image_metadata")
    )


def assign_model_split(df: DataFrame) -> DataFrame:
    return (
        df.withColumn(
            "model_split",
            F.when(
                F.col("dataset_split") == "test",
                F.lit("holdout_test"),
            )
            .when(
                F.pmod(F.xxhash64("image_id"), F.lit(10)) == 0,
                F.lit("val"),
            )
            .otherwise(F.lit("train")),
        )
        .withColumn(
            "negative_label_trust",
            F.when(F.col("has_annotation"), F.lit("partial"))
            .otherwise(F.lit("unknown")),
        )
    )


def create_manifest(
    spark: SparkSession,
    raw_dir: Path,
) -> DataFrame:
    train_images_df = build_image_metadata_df(spark, raw_dir / "train_images", "train")
    test_images_df = build_image_metadata_df(spark, raw_dir / "test_images", "test")
    image_df = train_images_df.unionByName(test_images_df)

    annotation_df = build_annotation_df(spark, raw_dir / "train.csv")

    manifest = (
        image_df.join(annotation_df, on="image_id", how="left")
        .fillna({"annotation_count": 0, "encoded_pixels_char_count": 0})
        .withColumn(
            "annotated_classes",
            F.when(F.col("annotated_classes").isNull(), F.array().cast("array<int>"))
            .otherwise(F.col("annotated_classes"))
        )
        .withColumn(
            "has_annotation",
            F.when(F.col("has_annotation").isNull(), F.lit(False)).otherwise(F.col("has_annotation"))
        )
    )

    manifest = enrich_with_dimensions(manifest)
    manifest = assign_model_split(manifest)

    return manifest.select(
        "image_id",
        "image_path",
        "dataset_split",
        "model_split",
        "width",
        "height",
        "file_size_bytes",
        "has_annotation",
        "annotation_count",
        "annotated_classes",
        "encoded_pixels_char_count",
        "negative_label_trust",
    )


def compute_stats(manifest: DataFrame) -> dict[str, object]:
    total_images = manifest.count()
    annotated_images = manifest.filter(F.col("has_annotation")).count()
    test_images = manifest.filter(F.col("dataset_split") == "test").count()

    split_rows = manifest.groupBy("model_split").count().collect()
    split_counts = {row["model_split"]: row["count"] for row in split_rows}

    class_rows = (
        manifest.filter(F.col("has_annotation"))
        .select(F.explode("annotated_classes").alias("class_id"))
        .groupBy("class_id")
        .count()
        .orderBy("class_id")
        .collect()
    )
    class_counts = {str(row["class_id"]): row["count"] for row in class_rows}

    return {
        "total_images": total_images,
        "annotated_images": annotated_images,
        "test_images": test_images,
        "model_split_counts": split_counts,
        "annotated_class_counts": class_counts,
        "label_caveat": "Unannotated regions should not be treated as trustworthy negative background.",
    }


def build_csv_manifest(manifest: DataFrame) -> DataFrame:
    return manifest.withColumn(
        "annotated_classes_csv",
        F.concat_ws(",", F.col("annotated_classes")),
    ).drop("annotated_classes")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Spark manifest for Severstal images.")
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=Path("data/raw/severstal-steel-defect-detection"),
        help="Path to raw Severstal dataset directory",
    )
    parser.add_argument(
        "--manifest-dir",
        type=Path,
        default=Path("data/manifests/severstal"),
        help="Directory to save manifest outputs",
    )
    args = parser.parse_args()

    spark = build_spark_session()
    try:
        manifest = create_manifest(spark, args.raw_dir)
        args.manifest_dir.mkdir(parents=True, exist_ok=True)

        csv_dir = args.manifest_dir / "manifest_csv"
        parquet_dir = args.manifest_dir / "manifest_parquet"
        stats_path = args.manifest_dir / "stats.json"

        csv_manifest = build_csv_manifest(manifest)

        csv_manifest.coalesce(1).write.mode("overwrite").option("header", True).csv(str(csv_dir))
        manifest.write.mode("overwrite").parquet(str(parquet_dir))

        stats = compute_stats(manifest)
        stats_path.write_text(json.dumps(stats, indent=2) + "\n")

        print(f"Saved CSV manifest to {csv_dir}")
        print(f"Saved Parquet manifest to {parquet_dir}")
        print(f"Saved stats to {stats_path}")
        print(json.dumps(stats, indent=2))
    finally:
        spark.stop()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
