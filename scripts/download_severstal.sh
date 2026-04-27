#!/usr/bin/env bash

set -euo pipefail

DATASET_SLUG="ayushcl/severstal-steel-defect-detection"
TARGET_DIR="data/raw/severstal-steel-defect-detection"

if ! command -v kaggle >/dev/null 2>&1; then
  echo "Kaggle CLI not found."
  echo "Install it with: pip install kaggle"
  echo "Then configure your Kaggle API token."
  exit 1
fi

mkdir -p "$TARGET_DIR"

echo "Downloading dataset files to $TARGET_DIR ..."
kaggle datasets download -d "$DATASET_SLUG" -p "$TARGET_DIR"

echo "Extracting archive ..."
find "$TARGET_DIR" -maxdepth 1 -name '*.zip' -exec unzip -o {} -d "$TARGET_DIR" \;

echo "Download and extraction complete."
