from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
from PIL import Image


def rle_decode(mask_rle: str, shape: tuple[int, int]) -> np.ndarray:
    tokens = mask_rle.split()
    starts = np.asarray(tokens[0::2], dtype=int) - 1
    lengths = np.asarray(tokens[1::2], dtype=int)
    ends = starts + lengths

    mask = np.zeros(shape[0] * shape[1], dtype=np.uint8)
    for start, end in zip(starts, ends):
        mask[start:end] = 1

    return mask.reshape(shape, order="F")


def load_row(csv_path: Path, row_index: int) -> dict[str, str]:
    with csv_path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    if row_index < 0 or row_index >= len(rows):
        raise IndexError(f"row_index {row_index} out of range for {len(rows)} rows")

    return rows[row_index]


def create_overlay(image: Image.Image, mask: np.ndarray) -> Image.Image:
    image_array = np.array(image).copy()
    overlay_color = np.array([255, 0, 0], dtype=np.uint8)

    image_array[mask == 1] = (
        0.6 * image_array[mask == 1] + 0.4 * overlay_color
    ).astype(np.uint8)

    return Image.fromarray(image_array)


def main() -> int:
    parser = argparse.ArgumentParser(description="Visualize a Severstal mask overlay.")
    parser.add_argument("csv_path", type=Path, help="Path to train.csv")
    parser.add_argument("image_dir", type=Path, help="Path to train_images directory")
    parser.add_argument("output_path", type=Path, help="Where to save the overlay image")
    parser.add_argument(
        "--row-index",
        type=int,
        default=0,
        help="Row index from train.csv to visualize",
    )
    args = parser.parse_args()

    row = load_row(args.csv_path, args.row_index)
    image_path = args.image_dir / row["ImageId"]

    image = Image.open(image_path).convert("RGB")
    width, height = image.size
    mask = rle_decode(row["EncodedPixels"], (height, width))
    overlay = create_overlay(image, mask)

    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    overlay.save(args.output_path)

    print(f"Saved overlay to {args.output_path}")
    print(
        {
            "image_id": row["ImageId"],
            "class_id": row["ClassId"],
            "image_size": {"width": width, "height": height},
            "mask_pixels": int(mask.sum()),
            "row_index": args.row_index,
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
