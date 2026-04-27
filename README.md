# Industrial AI Platform

Base project for a public portfolio platform focused on industrial computer vision, MLOps, and production-oriented AI systems.

## Day 1 scope

- Professional project skeleton
- Minimal FastAPI app
- `GET /health` endpoint
- First automated test with `pytest`
- Initial architecture documentation

## Project structure

```text
industrial-ai-platform/
├── app/
├── docs/
├── infra/
├── observability/
├── pipelines/
├── tests/
└── training/
```

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
make install
make api
make test
```

## Next milestone

Day 2 defines the public industrial dataset and the first ingestion flow.

Current dataset decision: `Severstal Steel Defect Detection`.
