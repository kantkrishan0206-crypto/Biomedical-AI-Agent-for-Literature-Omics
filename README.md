# Biomedical AI Agent for Literature + Omics

Research-grade biomedical AI systems engineering platform and internet-deployable SaaS application.

This repository implements a full-stack scientific operating system for literature reasoning, omics analysis, knowledge graph traversal, workflow DAG execution, experiment tracking, model governance, provenance, and real-time telemetry. The UI follows the supplied OMICS Codex cockpit reference: dark, dense, scientific, and operational.

## What Runs

- Frontend: Next.js 15, React, TypeScript, TailwindCSS, shadcn-style components, TanStack Query, Zustand, WebSockets, and SSE.
- Backend: FastAPI, async SQLAlchemy, Alembic, PostgreSQL, Redis/Celery, Qdrant, Ollama, LangGraph/LlamaIndex-ready orchestration.
- Data science: legal public metadata ingestion, user uploads, omics preprocessing, pathway/differential expression utilities, citation-grounded retrieval, provenance manifests.
- Operations: Docker Compose, Render backend config, Vercel frontend config, Prometheus, Grafana, Loki, OpenTelemetry, Kubernetes, Helm, Terraform templates.

## Quick Start

1. Copy environment templates:
   - Windows: `Copy-Item .env.local.example .env.local`
   - Linux/WSL2: `cp .env.local.example .env.local`
2. Install toolchains. Preferred path is WSL2 Ubuntu or Docker Desktop with WSL integration.
3. Start infrastructure: `docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build`
4. Run migrations: `make migrate`
5. Open frontend at `http://localhost:3000` and backend docs at `http://localhost:8000/docs`.

## Fixed Deployment Path

- Frontend: Vercel only.
- Backend: Render only.
- Database: PostgreSQL via `DATABASE_URL`; local development can be managed through pgAdmin4.
- Redis: Upstash via `REDIS_URL` in production.
- Inference: Ollama via `OLLAMA_BASE_URL`.

All secrets are environment-driven. Never commit real keys, URLs, tokens, auth secrets, or service credentials.

## Repository Map

The repo is organized as a monorepo with `frontend/`, `backend/`, `agents/`, `orchestration/`, `rag/`, `vector/`, `inference/`, `knowledge_graph/`, `experiments/`, `workflow_engine/`, `model_registry/`, `provenance/`, `notebooks/`, `data/`, `deployment/`, `monitoring/`, `kubernetes/`, `helm/`, `infra/`, `evaluation/`, `benchmarks/`, `results/`, and `tests/`.
