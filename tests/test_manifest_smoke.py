import csv
from pathlib import Path


def _get_manifest_csv_part() -> Path:
    csv_dir = Path("data/manifests/severstal/manifest_csv")
    return next(path for path in csv_dir.iterdir() if path.name.startswith("part-"))


def test_manifest_csv_exists_and_has_expected_columns() -> None:
    manifest_path = _get_manifest_csv_part()

    with manifest_path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        first_row = next(reader)

    expected_columns = {
        "image_id",
        "image_path",
        "dataset_split",
        "model_split",
        "width",
        "height",
        "file_size_bytes",
        "has_annotation",
        "annotation_count",
        "encoded_pixels_char_count",
        "negative_label_trust",
        "annotated_classes_csv",
    }

    assert set(first_row.keys()) == expected_columns
    assert first_row["image_id"].endswith(".jpg")
    assert first_row["dataset_split"] in {"train", "test"}
    assert first_row["model_split"] in {"train", "val", "holdout_test"}
