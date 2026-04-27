# Data Setup

This project uses the public `Severstal Steel Defect Detection` dataset as the initial industrial inspection dataset.
For operational simplicity, the initial download flow uses a public Kaggle dataset mirror instead of the original competition endpoint.

## Why this dataset

- Strong industrial framing for steel surface inspection
- Realistic defect segmentation problem
- Good portfolio signal for industrial computer vision

## Expected structure

```text
data/
├── raw/
│   └── severstal-steel-defect-detection/
├── processed/
├── manifests/
└── samples/
```

## Download options

### Option 1: Kaggle CLI

```bash
pip install kaggle
bash scripts/download_severstal.sh
```

### Option 2: Manual download

1. Open the dataset page on Kaggle.
2. Download the archive manually.
3. Extract it into:

```text
data/raw/severstal-steel-defect-detection/
```

## Validation

After the dataset is available locally:

```bash
.venv/bin/python scripts/validate_images.py data/raw/severstal-steel-defect-detection
```

The validation script checks:

- whether image files can be opened
- image dimensions
- zero-byte files
- non-image files with image suffixes

## Notes

- Raw dataset files are intentionally ignored by Git.
- This repository stores setup instructions and lightweight sample artifacts only.
- Kaggle terms and dataset license should be respected before redistribution.
- The current automation targets the mirror `ayushcl/severstal-steel-defect-detection`.

## Dataset limitations

- Visual inspection of sample overlays suggests that some images may contain additional visible defects beyond the annotated masks.
- Regions without masks should not be treated as guaranteed clean background.
- Missing annotation should be interpreted as "not labeled" rather than "confirmed negative".
- Any training or evaluation logic should document that label coverage may be incomplete.
