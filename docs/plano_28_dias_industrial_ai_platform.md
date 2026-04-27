# Plano de 28 Dias — Industrial AI Platform Enterprise MLOps

## Objetivo do projeto

Construir um projeto público, completo e defensável para GitHub e entrevistas:

> **Industrial AI Platform — Enterprise MLOps for Computer Vision**

A proposta é demonstrar uma arquitetura de IA em produção com visão computacional, MLOps, observabilidade, orquestração, segurança, cloud-ready deployment, documentação e narrativa de engenharia sênior.

## Resultado esperado ao final dos 28 dias

Você deve ter um repositório público com:

- Modelo de visão computacional treinado em dataset público industrial
- Pipeline de pré-processamento com Spark
- Orquestração com Airflow
- MLflow Tracking e Model Registry
- FastAPI para inferência
- PostgreSQL para logs de inferência
- Prometheus para métricas
- Grafana para dashboard
- Docker Compose funcional
- GitHub Actions CI/CD
- Kubernetes manifests
- Terraform AWS blueprint
- Autenticação via API Key ou JWT
- RBAC simples
- Alembic migrations
- Drift report com Evidently
- Load test com Locust ou K6
- Security scan no CI
- RAG assistant sobre a documentação do projeto
- Runbook operacional
- SLO/SLA básico
- Cost estimation AWS
- ADRs, docs e README forte
- Issues públicas no GitHub mostrando roadmap técnico

## Frase de posicionamento

> I build production-oriented AI systems, from computer vision models to deployable, monitored, cloud-ready and scalable ML services.

## Escopo técnico final

```text
Industrial AI Platform
├── Computer Vision model
├── Dataset público industrial
├── Spark preprocessing
├── Airflow orchestration
├── MLflow tracking + model registry
├── FastAPI inference service
├── PostgreSQL inference logging
├── Prometheus metrics
├── Grafana dashboard
├── Docker Compose
├── GitHub Actions CI/CD
├── Kubernetes manifests
├── Terraform AWS blueprint
├── JWT/API Key auth
├── RBAC simples
├── Alembic migrations
├── Evidently drift report
├── Locust/K6 load testing
├── Security scan
├── RAG assistant
├── Runbook
├── SLO/SLA
├── Cost estimation
├── Architecture docs
├── ADRs
└── README premium
```

## Estratégia de execução

Não tente deixar tudo perfeito antes de publicar. O repositório deve evoluir todo dia.

Regra:

> Todo dia precisa gerar pelo menos um commit útil.

O objetivo é mostrar consistência, engenharia e evolução incremental.

---

# Estrutura sugerida do repositório

```text
industrial-ai-platform/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── routes_health.py
│   │   ├── routes_predict.py
│   │   ├── routes_metrics.py
│   │   ├── routes_model.py
│   │   └── routes_rag.py
│   ├── auth/
│   │   ├── security.py
│   │   └── rbac.py
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   ├── inference/
│   │   ├── model_loader.py
│   │   └── predictor.py
│   ├── database/
│   │   ├── db.py
│   │   ├── models.py
│   │   └── migrations/
│   ├── monitoring/
│   │   └── prometheus.py
│   └── rag/
│       ├── ingest_docs.py
│       ├── retriever.py
│       └── assistant.py
├── training/
│   ├── train.py
│   ├── evaluate.py
│   ├── register_model.py
│   └── config.yaml
├── pipelines/
│   ├── airflow/
│   │   └── industrial_ai_training_dag.py
│   └── spark/
│       └── preprocess_images.py
├── infra/
│   ├── docker/
│   │   └── Dockerfile.api
│   ├── k8s/
│   │   ├── namespace.yaml
│   │   ├── api-deployment.yaml
│   │   ├── api-service.yaml
│   │   ├── postgres-deployment.yaml
│   │   ├── prometheus-config.yaml
│   │   └── grafana-deployment.yaml
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── README.md
├── observability/
│   ├── prometheus.yml
│   └── grafana-dashboard.json
├── load_tests/
│   └── locustfile.py
├── docs/
│   ├── architecture.md
│   ├── decisions.md
│   ├── production_readiness.md
│   ├── runbook.md
│   ├── aws_mapping.md
│   ├── cost_estimation.md
│   ├── slo_sla.md
│   └── adr/
│       ├── 0001-project-architecture.md
│       ├── 0002-mlflow-for-tracking.md
│       └── 0003-fastapi-for-serving.md
├── tests/
│   ├── test_health.py
│   ├── test_predict.py
│   ├── test_metrics.py
│   └── test_auth.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── docker-compose.yml
├── Makefile
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# Semana 1 — Core AI Platform

Objetivo da semana:

> Ter o sistema base funcionando: dataset, treino, MLflow, API, PostgreSQL e Docker Compose.

---

## Dia 1 — Criar repositório e base do projeto

### Objetivo

Criar o esqueleto profissional do projeto.

### Checklist

- [ ] Criar repositório no GitHub: `industrial-ai-platform`
- [ ] Criar estrutura de pastas
- [ ] Criar `README.md` inicial
- [ ] Criar `Makefile`
- [ ] Criar `requirements.txt` ou `pyproject.toml`
- [ ] Criar app FastAPI mínimo
- [ ] Criar endpoint `GET /health`
- [ ] Criar primeiro teste com `pytest`
- [ ] Criar primeira versão de `docs/architecture.md`
- [ ] Fazer primeiro commit público

### Comandos esperados

```bash
make install
make api
make test
```

### Commit sugerido

```text
init project structure with FastAPI health endpoint
```

### Issue GitHub sugerida

```text
[Core] Setup project skeleton and health endpoint
```

---

## Dia 2 — Definir dataset e preparar ingestão

### Objetivo

Escolher dataset público industrial e preparar a entrada de dados.

### Decisão prática

Prioridade:

1. NEU-DET se quiser detecção de defeitos
2. MVTec AD se quiser classificação/anomalia mais simples

Se NEU-DET atrasar, usar MVTec AD sem hesitar.

### Checklist

- [ ] Escolher dataset público
- [ ] Documentar decisão em `docs/decisions.md`
- [ ] Criar `data/README.md`
- [ ] Criar script de download ou instruções claras
- [ ] Separar amostras pequenas em `data/samples/`
- [ ] Criar estrutura `raw/processed/manifests`
- [ ] Criar validação básica de imagens
- [ ] Registrar limitações do dataset público

### Commit sugerido

```text
add public industrial dataset setup and data documentation
```

### Issue GitHub sugerida

```text
[Data] Add public industrial dataset setup
```

---

## Dia 3 — Spark preprocessing

### Objetivo

Criar pipeline de pré-processamento com PySpark.

### Checklist

- [ ] Criar `pipelines/spark/preprocess_images.py`
- [ ] Ler metadata das imagens
- [ ] Validar arquivos
- [ ] Gerar manifest CSV/Parquet
- [ ] Criar split train/val/test
- [ ] Salvar estatísticas do dataset
- [ ] Documentar por que Spark foi incluído
- [ ] Criar teste simples para manifest

### Observação

Spark aqui não precisa processar terabytes. Ele demonstra padrão de engenharia para pipeline de dados escalável.

### Commit sugerido

```text
add spark preprocessing pipeline for image manifests
```

### Issue GitHub sugerida

```text
[Data] Implement Spark preprocessing job
```

---

## Dia 4 — Treinamento v1

### Objetivo

Treinar primeiro modelo funcional.

### Checklist

- [ ] Criar `training/train.py`
- [ ] Criar `training/config.yaml`
- [ ] Implementar treino baseline
- [ ] Salvar modelo em `models/`
- [ ] Calcular métricas básicas
- [ ] Criar `training/evaluate.py`
- [ ] Gerar confusion matrix ou métrica equivalente
- [ ] Documentar baseline

### Métricas mínimas

- [ ] Accuracy ou mAP
- [ ] Precision
- [ ] Recall
- [ ] F1-score
- [ ] Latência média
- [ ] Tamanho do modelo

### Commit sugerido

```text
add baseline computer vision training pipeline
```

### Issue GitHub sugerida

```text
[Training] Add baseline CV model training
```

---

## Dia 5 — MLflow Tracking

### Objetivo

Adicionar rastreabilidade de experimentos.

### Checklist

- [ ] Configurar MLflow local
- [ ] Logar parâmetros do treino
- [ ] Logar métricas
- [ ] Logar artifacts
- [ ] Logar modelo
- [ ] Adicionar MLflow ao Docker Compose se possível
- [ ] Atualizar README com instrução de uso
- [ ] Tirar print da tela do MLflow para `docs/images/`

### Parâmetros para logar

- [ ] Dataset version
- [ ] Model name
- [ ] Image size
- [ ] Epochs
- [ ] Batch size
- [ ] Learning rate
- [ ] Git commit hash, se possível

### Commit sugerido

```text
integrate mlflow experiment tracking
```

### Issue GitHub sugerida

```text
[MLOps] Add MLflow tracking
```

---

## Dia 6 — FastAPI inference + model loader

### Objetivo

Transformar modelo em serviço.

### Checklist

- [ ] Criar `app/inference/model_loader.py`
- [ ] Criar `app/inference/predictor.py`
- [ ] Criar endpoint `POST /predict`
- [ ] Criar endpoint `GET /model/info`
- [ ] Medir latência da inferência
- [ ] Retornar classe, confiança, versão do modelo e latência
- [ ] Validar upload de imagem
- [ ] Criar testes mínimos da API

### Resposta esperada de `/predict`

```json
{
  "prediction": "defect",
  "confidence": 0.94,
  "model_version": "v1.0.0",
  "latency_ms": 37.2,
  "request_id": "abc123"
}
```

### Commit sugerido

```text
add FastAPI model inference endpoints
```

### Issue GitHub sugerida

```text
[Serving] Implement model inference API
```

---

## Dia 7 — PostgreSQL inference logging + Docker Compose base

### Objetivo

Salvar logs de inferência e rodar serviços básicos via Docker Compose.

### Checklist

- [ ] Adicionar PostgreSQL ao `docker-compose.yml`
- [ ] Criar conexão com banco
- [ ] Criar tabela `inference_logs`
- [ ] Salvar toda inferência no banco
- [ ] Adicionar endpoint básico `GET /metrics`
- [ ] Criar Dockerfile da API
- [ ] Rodar `docker compose up --build`
- [ ] Atualizar README com instruções

### Campos da tabela

- [ ] id
- [ ] request_id
- [ ] timestamp
- [ ] filename
- [ ] predicted_class
- [ ] confidence
- [ ] latency_ms
- [ ] model_version

### Commit sugerido

```text
add postgres inference logging and docker compose setup
```

### Issue GitHub sugerida

```text
[Serving] Add inference logging with PostgreSQL
```

---

# Semana 2 — MLOps, Observabilidade e Orquestração

Objetivo da semana:

> Transformar o app em um pipeline de ML operável, monitorável e orquestrado.

---

## Dia 8 — MLflow Model Registry e promoção de modelo

### Objetivo

Criar fluxo de registry e promoção de modelo.

### Checklist

- [ ] Criar `training/register_model.py`
- [ ] Registrar modelo no MLflow Model Registry
- [ ] Criar estágios `Staging` e `Production`
- [ ] Criar regra simples de promoção
- [ ] Promover modelo apenas se métrica mínima for atingida
- [ ] Documentar model promotion gate
- [ ] Atualizar `docs/production_readiness.md`

### Exemplo de regra

```text
Promote to Production if:
F1-score >= 0.85
and average latency <= 100 ms
```

### Commit sugerido

```text
add mlflow model registry promotion workflow
```

### Issue GitHub sugerida

```text
[MLOps] Add model registry and promotion gate
```

---

## Dia 9 — Prometheus metrics

### Objetivo

Expor métricas reais da API.

### Checklist

- [ ] Criar `app/monitoring/prometheus.py`
- [ ] Expor endpoint `/metrics`
- [ ] Medir total de inferências
- [ ] Medir latência
- [ ] Medir confiança média
- [ ] Medir erros da API
- [ ] Medir distribuição de classes
- [ ] Adicionar Prometheus ao Docker Compose
- [ ] Criar `observability/prometheus.yml`

### Métricas mínimas

```text
inference_count_total
inference_latency_seconds
prediction_confidence
prediction_class_count
api_errors_total
```

### Commit sugerido

```text
add prometheus metrics for inference service
```

### Issue GitHub sugerida

```text
[Observability] Add Prometheus metrics
```

---

## Dia 10 — Grafana dashboard

### Objetivo

Criar visualização operacional.

### Checklist

- [ ] Adicionar Grafana ao Docker Compose
- [ ] Criar dashboard JSON
- [ ] Mostrar total de inferências
- [ ] Mostrar latência média
- [ ] Mostrar p95 se possível
- [ ] Mostrar distribuição de classes
- [ ] Mostrar erros
- [ ] Mostrar confiança média
- [ ] Tirar print do dashboard
- [ ] Atualizar README

### Commit sugerido

```text
add grafana dashboard for inference monitoring
```

### Issue GitHub sugerida

```text
[Observability] Add Grafana dashboard
```

---

## Dia 11 — Airflow DAG

### Objetivo

Orquestrar o ciclo de ML.

### Checklist

- [ ] Criar `pipelines/airflow/industrial_ai_training_dag.py`
- [ ] Criar task `validate_dataset`
- [ ] Criar task `preprocess_with_spark`
- [ ] Criar task `train_model`
- [ ] Criar task `evaluate_model`
- [ ] Criar task `register_model`
- [ ] Documentar fluxo da DAG
- [ ] Adicionar Airflow ao Compose se não deixar pesado demais
- [ ] Se ficar pesado, documentar execução separada

### DAG esperada

```text
validate_dataset
   ↓
preprocess_with_spark
   ↓
train_model
   ↓
evaluate_model
   ↓
register_model
```

### Commit sugerido

```text
add airflow dag for ml training pipeline
```

### Issue GitHub sugerida

```text
[Pipeline] Add Airflow orchestration DAG
```

---

## Dia 12 — Structured logging e error handling

### Objetivo

Deixar a API com cara de produção.

### Checklist

- [ ] Implementar logs em JSON
- [ ] Criar request_id por requisição
- [ ] Padronizar erros
- [ ] Logar exceções
- [ ] Logar latência
- [ ] Criar middleware básico
- [ ] Criar documentação de logging
- [ ] Atualizar testes

### Commit sugerido

```text
add structured logging and API error handling
```

### Issue GitHub sugerida

```text
[Core] Add structured logging and error handling
```

---

## Dia 13 — RAG assistant sobre documentação

### Objetivo

Adicionar módulo GenAI útil, sem virar projeto paralelo.

### Checklist

- [ ] Criar `app/rag/ingest_docs.py`
- [ ] Criar `app/rag/retriever.py`
- [ ] Criar `app/rag/assistant.py`
- [ ] Indexar README e docs
- [ ] Criar endpoint `POST /rag/query`
- [ ] Retornar resposta com fontes
- [ ] Documentar limitações
- [ ] Adicionar teste simples

### Documentos a indexar

- [ ] README.md
- [ ] docs/architecture.md
- [ ] docs/decisions.md
- [ ] docs/production_readiness.md
- [ ] docs/aws_mapping.md

### Commit sugerido

```text
add documentation RAG assistant endpoint
```

### Issue GitHub sugerida

```text
[GenAI] Add RAG assistant over project docs
```

---

## Dia 14 — Consolidação da semana 2

### Objetivo

Garantir que a plataforma base está coerente.

### Checklist

- [ ] Rodar Docker Compose completo
- [ ] Testar `/health`
- [ ] Testar `/predict`
- [ ] Testar `/model/info`
- [ ] Testar `/metrics`
- [ ] Testar `/rag/query`
- [ ] Abrir MLflow UI
- [ ] Abrir Grafana
- [ ] Revisar README
- [ ] Criar prints em `docs/images/`
- [ ] Criar release tag `v0.2.0`

### Commit sugerido

```text
stabilize core mlops platform v0.2
```

### Issue GitHub sugerida

```text
[Release] Stabilize v0.2 core MLOps platform
```

---

# Semana 3 — Enterprise Hardening

Objetivo da semana:

> Adicionar segurança, governança, CI/CD, Kubernetes, Terraform, drift, load test e readiness.

---

## Dia 15 — Autenticação API Key/JWT

### Objetivo

Proteger endpoints principais.

### Checklist

- [ ] Implementar API Key ou JWT
- [ ] Proteger `/predict`
- [ ] Proteger `/model/info` se necessário
- [ ] Deixar `/health` público
- [ ] Configurar secrets via env var
- [ ] Criar teste para acesso autorizado
- [ ] Criar teste para acesso negado
- [ ] Atualizar docs

### Decisão recomendada

Começar com API Key. Mais simples e suficiente para portfólio.

### Commit sugerido

```text
add api key authentication for protected endpoints
```

### Issue GitHub sugerida

```text
[Security] Add API authentication
```

---

## Dia 16 — RBAC simples

### Objetivo

Criar papéis básicos de acesso.

### Checklist

- [ ] Criar roles `admin`, `operator`, `viewer`
- [ ] Definir permissões por endpoint
- [ ] Implementar dependency de autorização
- [ ] Criar testes de permissão
- [ ] Documentar matriz de acesso

### Matriz sugerida

```text
admin: all endpoints
operator: predict, metrics, model info
viewer: health, metrics, model info
```

### Commit sugerido

```text
add simple rbac authorization layer
```

### Issue GitHub sugerida

```text
[Security] Add simple RBAC
```

---

## Dia 17 — Alembic migrations

### Objetivo

Profissionalizar evolução do banco.

### Checklist

- [ ] Instalar/configurar Alembic
- [ ] Criar migration inicial
- [ ] Criar migration da tabela `inference_logs`
- [ ] Documentar comandos
- [ ] Ajustar Docker Compose para rodar migrations
- [ ] Testar banco do zero

### Commit sugerido

```text
add alembic database migrations
```

### Issue GitHub sugerida

```text
[Database] Add Alembic migrations
```

---

## Dia 18 — Evidently drift report

### Objetivo

Adicionar monitoramento de qualidade/distribuição de dados.

### Checklist

- [ ] Adicionar Evidently
- [ ] Criar script `monitoring/generate_drift_report.py`
- [ ] Comparar referência vs dados recentes
- [ ] Gerar HTML report
- [ ] Salvar artifact em `reports/`
- [ ] Documentar o que é drift
- [ ] Explicar limitações em dataset público

### Drift mínimo

- [ ] Distribuição de confidence
- [ ] Distribuição de classes
- [ ] Latência
- [ ] Métricas de entrada se disponíveis

### Commit sugerido

```text
add evidently drift monitoring report
```

### Issue GitHub sugerida

```text
[Monitoring] Add drift report with Evidently
```

---

## Dia 19 — Load testing com Locust ou K6

### Objetivo

Mostrar noção de escala e performance.

### Checklist

- [ ] Criar `load_tests/locustfile.py` ou script K6
- [ ] Testar endpoint `/predict`
- [ ] Gerar métricas de throughput
- [ ] Registrar p50/p95/p99
- [ ] Documentar resultado
- [ ] Criar seção no README
- [ ] Salvar print ou log do teste

### Métricas

- [ ] Requests por segundo
- [ ] Latência média
- [ ] Latência p95
- [ ] Latência p99
- [ ] Taxa de erro

### Commit sugerido

```text
add load testing for inference endpoint
```

### Issue GitHub sugerida

```text
[Performance] Add load testing suite
```

---

## Dia 20 — GitHub Actions CI/CD + security scan

### Objetivo

Criar pipeline real de validação.

### Checklist

- [ ] Criar `.github/workflows/ci.yml`
- [ ] Rodar lint com Ruff
- [ ] Rodar testes com Pytest
- [ ] Rodar build Docker
- [ ] Rodar pip-audit ou safety
- [ ] Rodar Trivy se possível
- [ ] Adicionar badge no README
- [ ] Corrigir falhas

### Pipeline mínimo

```text
checkout
setup python
install dependencies
ruff
pytest
docker build
security scan
```

### Commit sugerido

```text
add ci pipeline with tests lint docker build and security scan
```

### Issue GitHub sugerida

```text
[CI/CD] Add GitHub Actions pipeline
```

---

## Dia 21 — Kubernetes manifests

### Objetivo

Mostrar arquitetura cloud-native.

### Checklist

- [ ] Criar namespace
- [ ] Criar deployment da API
- [ ] Criar service da API
- [ ] Criar deployment do PostgreSQL
- [ ] Criar config map do Prometheus
- [ ] Criar deployment do Grafana
- [ ] Criar README de deploy local com kind/minikube
- [ ] Documentar que EKS é blueprint, não deploy ativo

### Commit sugerido

```text
add kubernetes manifests for platform services
```

### Issue GitHub sugerida

```text
[Infra] Add Kubernetes manifests
```

---

# Semana 4 — Cloud Blueprint, Documentação e Mercado

Objetivo da semana:

> Finalizar o projeto como ativo de carreira e deixá-lo pronto para recrutadores e entrevistas.

---

## Dia 22 — Terraform AWS blueprint

### Objetivo

Criar blueprint cloud realista, sem gerar custo por acidente.

### Checklist

- [ ] Criar `infra/terraform/main.tf`
- [ ] Criar `variables.tf`
- [ ] Criar `outputs.tf`
- [ ] Mapear ECR
- [ ] Mapear ECS ou EKS
- [ ] Mapear S3
- [ ] Mapear RDS PostgreSQL
- [ ] Mapear CloudWatch
- [ ] Mapear IAM roles
- [ ] Escrever README com aviso de segurança/custos
- [ ] Não aplicar infra real por padrão

### Frase obrigatória

```text
This Terraform module is a cloud deployment blueprint and is not applied by default.
```

### Commit sugerido

```text
add terraform aws deployment blueprint
```

### Issue GitHub sugerida

```text
[Infra] Add Terraform AWS blueprint
```

---

## Dia 23 — AWS mapping e cost estimation

### Objetivo

Conectar projeto com cloud e visão de negócio.

### Checklist

- [ ] Criar `docs/aws_mapping.md`
- [ ] Criar `docs/cost_estimation.md`
- [ ] Mapear local para AWS
- [ ] Estimar custo mensal básico
- [ ] Explicar trade-offs de ECS vs EKS
- [ ] Explicar S3, ECR, RDS, CloudWatch
- [ ] Explicar alternativas mais baratas

### Mapeamento esperado

```text
Docker image -> ECR
FastAPI service -> ECS/EKS
PostgreSQL -> RDS
MLflow artifacts -> S3
Metrics/logs -> CloudWatch/Prometheus
Training pipeline -> SageMaker Pipelines
Batch inference -> SageMaker Batch Transform
```

### Commit sugerido

```text
document aws deployment mapping and cost estimation
```

### Issue GitHub sugerida

```text
[Docs] Add AWS mapping and cost estimation
```

---

## Dia 24 — Runbook operacional

### Objetivo

Mostrar maturidade de operação.

### Checklist

- [ ] Criar `docs/runbook.md`
- [ ] Documentar como subir ambiente
- [ ] Documentar como treinar modelo
- [ ] Documentar como promover modelo
- [ ] Documentar como checar logs
- [ ] Documentar como checar métricas
- [ ] Documentar troubleshooting
- [ ] Documentar rollback manual

### Seções do runbook

```text
Start services
Train model
Register model
Promote model
Check API health
Check inference logs
Check Prometheus metrics
Check Grafana dashboard
Common failures
Rollback procedure
```

### Commit sugerido

```text
add production runbook
```

### Issue GitHub sugerida

```text
[Docs] Add production runbook
```

---

## Dia 25 — SLO/SLA e production readiness

### Objetivo

Mostrar que você pensa como engenheiro de produção.

### Checklist

- [ ] Criar `docs/slo_sla.md`
- [ ] Criar ou finalizar `docs/production_readiness.md`
- [ ] Definir latência alvo
- [ ] Definir disponibilidade alvo
- [ ] Definir taxa de erro aceitável
- [ ] Definir critérios de promoção de modelo
- [ ] Definir critérios de rollback
- [ ] Criar checklist de produção

### Exemplo de SLO

```text
Availability target: 99.0% for reference deployment
Latency target: p95 < 300 ms for /predict
Error rate target: < 1%
Model confidence monitoring enabled
Manual rollback available through model version pinning
```

### Commit sugerido

```text
add slo sla and production readiness documentation
```

### Issue GitHub sugerida

```text
[Docs] Add SLO/SLA and production readiness checklist
```

---

## Dia 26 — ADRs e decisões arquiteturais

### Objetivo

Documentar pensamento sênior.

### Checklist

- [ ] Criar pasta `docs/adr/`
- [ ] Criar ADR sobre FastAPI
- [ ] Criar ADR sobre MLflow
- [ ] Criar ADR sobre Docker Compose local-first
- [ ] Criar ADR sobre Prometheus/Grafana
- [ ] Criar ADR sobre Airflow/Spark
- [ ] Criar ADR sobre Terraform blueprint
- [ ] Criar ADR sobre RAG assistant

### Formato de ADR

```text
# ADR-0001: Use FastAPI for model serving

## Status
Accepted

## Context
...

## Decision
...

## Consequences
...
```

### Commit sugerido

```text
add architecture decision records
```

### Issue GitHub sugerida

```text
[Docs] Add architecture decision records
```

---

## Dia 27 — README premium e evidências

### Objetivo

Transformar o projeto em vitrine.

### Checklist

- [ ] Reescrever README do zero se necessário
- [ ] Adicionar diagrama de arquitetura
- [ ] Adicionar badges
- [ ] Adicionar prints
- [ ] Adicionar quickstart
- [ ] Adicionar endpoints
- [ ] Adicionar seção de produção
- [ ] Adicionar seção de segurança
- [ ] Adicionar seção de observabilidade
- [ ] Adicionar seção de cloud deployment blueprint
- [ ] Adicionar roadmap
- [ ] Revisar inglês
- [ ] Abrir issues públicas de próximos passos

### Seções obrigatórias do README

```text
Overview
Why this project exists
Architecture
Tech Stack
Quickstart
API Endpoints
Training Pipeline
MLflow Tracking
Model Registry
Inference Logging
Observability
Airflow Orchestration
Spark Preprocessing
Security
Kubernetes
Terraform AWS Blueprint
RAG Assistant
Production Readiness
Limitations
Roadmap
```

### Commit sugerido

```text
polish README and project evidence for public release
```

### Issue GitHub sugerida

```text
[Release] Polish README and public project evidence
```

---

## Dia 28 — Release final, LinkedIn, CV e candidatura

### Objetivo

Transformar o projeto em ativo de carreira.

### Checklist

- [ ] Criar release `v1.0.0`
- [ ] Revisar repositório público
- [ ] Fixar repo no GitHub profile
- [ ] Atualizar LinkedIn
- [ ] Atualizar CV
- [ ] Escrever post curto no LinkedIn
- [ ] Criar mensagem padrão para recrutadores
- [ ] Separar 10 vagas para aplicar
- [ ] Aplicar para primeiras vagas
- [ ] Criar issue de roadmap pós-v1

### Descrição do projeto no CV

```text
Industrial AI Platform — Enterprise MLOps for Computer Vision

Built a production-oriented Industrial AI platform combining computer vision model training,
Spark-based preprocessing, Airflow orchestration, MLflow experiment tracking and model registry,
Dockerized FastAPI inference, PostgreSQL inference logging, Prometheus/Grafana observability,
API authentication, RBAC, drift monitoring, load testing, Kubernetes manifests, Terraform AWS
blueprint, GitHub Actions CI/CD and a lightweight RAG assistant for operational documentation.
```

### Headline LinkedIn

```text
Machine Learning Engineer | Computer Vision | Edge AI | MLOps | Industrial AI Systems
```

### About LinkedIn

```text
I build production-oriented AI systems, with a strong background in computer vision,
edge deployment, model optimization and industrial integration.

My work focuses on taking models beyond notebooks: building deployable APIs,
tracking experiments, versioning models, monitoring inference, integrating with real systems
and designing cloud-ready ML architectures.

I recently built a public Industrial AI Platform project combining computer vision,
Spark preprocessing, Airflow orchestration, MLflow, FastAPI, PostgreSQL, Docker,
Prometheus/Grafana, Kubernetes manifests, Terraform AWS blueprint, CI/CD, security hardening
and a lightweight RAG assistant.
```

### Mensagem para recrutador

```text
Hi, I’m a Computer Vision / Machine Learning Engineer with hands-on experience deploying
AI systems in real industrial environments.

I recently published an Industrial AI Platform project demonstrating production-oriented
ML engineering: computer vision training, MLflow tracking, model registry, FastAPI serving,
PostgreSQL inference logging, Prometheus/Grafana observability, Airflow orchestration,
Spark preprocessing, Kubernetes manifests, Terraform AWS blueprint and CI/CD.

I’m looking for ML Engineer / Applied AI Engineer roles where I can help take models
from prototype to production.
```

### Commit sugerido

```text
release v1.0 industrial ai platform
```

### Issue GitHub sugerida

```text
[Release] Publish v1.0 and update career assets
```

---

# Checklist final do projeto

## Core ML

- [ ] Dataset público industrial
- [ ] Pré-processamento
- [ ] Treinamento
- [ ] Avaliação
- [ ] Métricas
- [ ] Modelo salvo
- [ ] MLflow Tracking
- [ ] Model Registry
- [ ] Promotion gate

## Serving

- [ ] FastAPI
- [ ] `/health`
- [ ] `/predict`
- [ ] `/model/info`
- [ ] `/metrics`
- [ ] `/rag/query`
- [ ] Model loader
- [ ] Latência medida
- [ ] Resposta padronizada

## Database

- [ ] PostgreSQL
- [ ] Inference logs
- [ ] Alembic migrations
- [ ] Model version no log
- [ ] Request ID

## Observability

- [ ] Prometheus
- [ ] Grafana
- [ ] Latência
- [ ] Erros
- [ ] Contagem de inferências
- [ ] Distribuição de classes
- [ ] Drift report

## Pipeline

- [ ] Spark preprocessing
- [ ] Airflow DAG
- [ ] Training task
- [ ] Evaluation task
- [ ] Register model task

## Enterprise

- [ ] API Key ou JWT
- [ ] RBAC
- [ ] Structured logging
- [ ] Error handling
- [ ] Load test
- [ ] Security scan
- [ ] CI/CD

## Infra

- [ ] Dockerfile
- [ ] Docker Compose
- [ ] Kubernetes manifests
- [ ] Terraform AWS blueprint
- [ ] AWS mapping
- [ ] Cost estimation

## Docs

- [ ] README forte
- [ ] Architecture docs
- [ ] Decisions docs
- [ ] ADRs
- [ ] Runbook
- [ ] SLO/SLA
- [ ] Production readiness
- [ ] Prints
- [ ] Roadmap

---

# Estratégia diária de GitHub

## Todo dia

- [ ] Criar ou atualizar issue
- [ ] Criar branch curta
- [ ] Fazer commits pequenos
- [ ] Atualizar README/docs
- [ ] Abrir PR, mesmo que seja você mesmo
- [ ] Fazer merge
- [ ] Deixar histórico limpo

## Padrão de branch

```text
feature/day-01-project-skeleton
feature/day-02-dataset-setup
feature/day-03-spark-preprocessing
...
```

## Padrão de commit

```text
add ...
implement ...
document ...
fix ...
refactor ...
```

## Padrão de PR

```text
## What changed
- ...

## Why
- ...

## How to test
- ...

## Screenshots
- ...
```

---

# Estratégia de uso do Codex

## Não pedir tudo de uma vez

Trabalhe por dia e por módulo.

Todo prompt deve pedir:

- implementação
- testes
- atualização de docs
- preservação da arquitetura
- instrução de como rodar
- checklist do que foi feito

## Prompt base

```text
You are a senior Machine Learning Engineer and MLOps Architect.

We are building a public portfolio project called Industrial AI Platform:
Enterprise MLOps for Computer Vision.

The goal is to demonstrate production-oriented AI engineering using computer vision,
Spark, Airflow, MLflow, FastAPI, PostgreSQL, Docker, Prometheus/Grafana,
Kubernetes manifests, Terraform AWS blueprint, GitHub Actions, security hardening,
drift monitoring, load testing and a lightweight RAG assistant.

Implement today's module with clean architecture, typed Python, meaningful tests,
clear documentation updates and production-oriented decisions.

Do not overengineer. Build a working vertical slice.
Prefer simple, robust and explainable code.
Update README/docs when relevant.
```

---

# Critério de sucesso

O plano deu certo se, ao final de 28 dias, o projeto parecer:

> uma referência pública de como estruturar uma aplicação de IA industrial em produção.

Não precisa ser uma plataforma enterprise real operando com clientes.

Precisa ser:

- funcional
- bem arquitetado
- documentado
- demonstrável
- defensável tecnicamente
- alinhado com vagas de ML Engineer / AI Engineer / MLOps

## Framing correto

Não vender como:

> Enterprise platform production-ready for Fortune 500.

Vender como:

> Enterprise-grade reference architecture implemented as a working vertical slice.

Essa frase é forte, honesta e defensável.

---

# Próximo passo depois dos 28 dias

## Semana seguinte

- [ ] Fazer simulados AWS Machine Learning Engineer Associate
- [ ] Agendar prova quando estiver acima de 75–80%
- [ ] Aplicar para vagas
- [ ] Criar mini vídeo demo do projeto
- [ ] Melhorar GitHub profile README
- [ ] Fazer segundo projeto menor de RAG ou deploy AWS real parcial

## Certificação

A certificação AWS entra como selo de validação do pacote:

```text
experiência real industrial
+
projeto público enterprise-grade
+
certificação AWS ML Engineer Associate
+
narrativa de produção
```

Esse é o posicionamento forte.
