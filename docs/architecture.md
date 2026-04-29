# Architecture v0.1

## Goal

Create a production-oriented public portfolio project for industrial computer vision with a clean evolution path toward MLOps, observability, orchestration, and deployment.

## Initial components

- `app/`: FastAPI service exposing health and future inference endpoints
- `training/`: model training and evaluation workflows
- `pipelines/`: orchestration layer for scheduled or batch jobs
- `infra/`: container and infrastructure definitions
- `observability/`: monitoring configuration and dashboards
- `docs/`: architecture, setup, and operational notes

## Day 1 runtime path

1. FastAPI starts from `app.main`.
2. The `/health` route confirms the API process is running.
3. `pytest` validates the first service contract.

## Planned evolution

- Day 2: dataset definition and ingestion
- Day 3+: training pipeline, experiment tracking, and model-serving flow
- Later phases: API auth, metrics, Airflow, CI/CD, Kubernetes, and cloud blueprint

## Why Spark is included

Spark is used here as a data-engineering layer for reproducible preprocessing and manifest generation.

Even though this project does not require massive scale on day one, Spark demonstrates:

- a structured batch-processing pattern
- scalable tabular transformations over dataset metadata
- a clear separation between raw files and curated manifests
- an engineering path that can grow from local execution to larger environments

In this project, Spark is not included to claim big data volume.
It is included to show how an industrial AI platform can organize image metadata, labels, splits, and dataset statistics using a production-friendly data pipeline style.
