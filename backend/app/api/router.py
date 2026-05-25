from __future__ import annotations

from fastapi import APIRouter

from app.api import admin, agents, api_keys, auth, billing, datasets, experiments, health, knowledge_graph, notebook, projects, quotas, reports, retrieval, telemetry, workflows, workspaces

api_router = APIRouter(prefix="/api/v1")
for router in [
    health.router,
    auth.router,
    projects.router,
    workspaces.router,
    datasets.router,
    workflows.router,
    agents.router,
    retrieval.router,
    reports.router,
    experiments.router,
    knowledge_graph.router,
    telemetry.router,
    notebook.router,
    admin.router,
    billing.router,
    api_keys.router,
    quotas.router,
]:
    api_router.include_router(router)
