# Dataset Decisions

## 2026-04-27 - Day 2 dataset selection

### Chosen dataset

`Severstal Steel Defect Detection`

### Why this was selected

- It communicates a concrete industrial inspection use case.
- It matches the project theme of production-oriented computer vision for manufacturing.
- It creates room to demonstrate segmentation, data ingestion, manifests, training, and later deployment.

### Tradeoffs accepted

- The original source is a Kaggle competition, which adds access friction.
- The current setup uses a public Kaggle dataset mirror for easier automation.
- Setup depends on Kaggle credentials for automated download.
- The repository should not include the raw dataset itself.
- Visual review suggests annotation coverage may be incomplete for some images.

### Practical impact

- Day 2 focuses on reproducible dataset setup rather than bundling data.
- Day 3 can build preprocessing on top of a known raw folder layout.
- Source provenance should be documented clearly in the repository.
- Unannotated regions must not be assumed to be trustworthy negative background during preprocessing or training.
