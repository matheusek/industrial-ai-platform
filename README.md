# Industrial AI Platform

Production-oriented portfolio project for industrial computer vision, MLOps, and AI platform engineering.

## Overview

This repository is being built as a public end-to-end Industrial AI platform focused on:

- industrial defect inspection
- computer vision model training
- reproducible data and MLOps workflows
- API-based model serving
- observability and production-oriented engineering patterns

The goal is not just to train a model, but to present a realistic platform structure that looks closer to a deployable industrial AI system.

## Current status

- FastAPI service scaffold created
- `GET /health` endpoint implemented
- First automated test with `pytest`
- Initial architecture documentation added
- Public industrial dataset selected and ingested
- Dataset validation and mask visualization utilities implemented

## Dataset

Current dataset: `Severstal Steel Defect Detection`

Why it was selected:

- strong industrial manufacturing context
- realistic surface defect segmentation problem
- good portfolio signal for industrial computer vision

Important limitation:

- visual inspection suggests annotation coverage may be incomplete in some images
- unlabeled regions should not be treated as guaranteed defect-free background

More details:

- [data/README.md](/home/matheus/industrial-ai-platform/data/README.md)
- [docs/decisions.md](/home/matheus/industrial-ai-platform/docs/decisions.md)

## Core stack

- Python
- FastAPI
- pytest
- Pillow
- NumPy

Planned additions across the roadmap:

- MLflow
- PostgreSQL
- Docker Compose
- Prometheus and Grafana
- Airflow
- Kubernetes
- Terraform

## Project structure

```text
industrial-ai-platform/
├── app/              # API service
├── data/             # dataset setup, samples, manifests
├── docs/             # architecture and decisions
├── infra/            # deployment and infrastructure assets
├── observability/    # monitoring assets
├── pipelines/        # orchestration and preprocessing
├── scripts/          # utility scripts
├── tests/            # automated tests
└── training/         # training workflows
```

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
make install
make api
make test
```

API health endpoint:

```text
GET /health
```

## Documentation

- [docs/architecture.md](/home/matheus/industrial-ai-platform/docs/architecture.md)
- [docs/decisions.md](/home/matheus/industrial-ai-platform/docs/decisions.md)
- [docs/plano_28_dias_industrial_ai_platform.md](/home/matheus/industrial-ai-platform/docs/plano_28_dias_industrial_ai_platform.md)

## Roadmap

- Core API and project skeleton
- Dataset ingestion and validation
- Preprocessing and manifest generation
- Training and experiment tracking
- Model serving and monitoring
- CI/CD, orchestration, and infrastructure blueprint
