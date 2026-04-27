from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, UnidentifiedImageError


def validate_image(path: Path) -> tuple[bool, str]:
    if path.stat().st_size == 0:
        return False, "zero-byte file"

    try:
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            width, height = image.size
    except UnidentifiedImageError:
        return False, "unidentified image"
    except OSError as exc:
        return False, f"os error: {exc}"

    return True, f"{width}x{height}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate image files in a dataset directory.")
    parser.add_argument("dataset_dir", type=Path, help="Path to the dataset directory to inspect.")
    args = parser.parse_args()

    if not args.dataset_dir.exists():
        print(f"Dataset directory not found: {args.dataset_dir}")
        return 1

    image_files = sorted(
        path for path in args.dataset_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg", ".png", ".bmp"}
    )

    if not image_files:
        print("No image files found.")
        return 1

    invalid = []
    for path in image_files:
        is_valid, details = validate_image(path)
        if not is_valid:
            invalid.append((path, details))

    print(f"Checked {len(image_files)} image files.")
    print(f"Invalid files: {len(invalid)}")

    for path, details in invalid[:20]:
        print(f"- {path}: {details}")

    return 0 if not invalid else 2


if __name__ == "__main__":
    raise SystemExit(main())
