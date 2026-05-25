#!/usr/bin/env bash
set -euo pipefail
echo "[biomedical-ai] $0"
pnpm install --frozen-lockfile=false && pnpm build
python3 -m compileall backend agents orchestration rag vector inference knowledge_graph experiments workflow_engine model_registry provenance notebooks
