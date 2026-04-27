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
