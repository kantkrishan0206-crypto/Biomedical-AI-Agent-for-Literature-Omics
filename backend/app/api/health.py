from __future__ import annotations

from fastapi import APIRouter

from app.core.config import get_settings
from app.core.observability import metrics_response

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
async def health() -> dict:
    settings = get_settings()
    return {"status": "ok", "service": settings.app_name, "owner": settings.app_owner_email}


@router.get("/ready")
async def ready() -> dict:
    return {"status": "ready", "dependencies": ["postgresql", "redis", "qdrant", "ollama"]}


@router.get("/metrics")
async def metrics():
    return metrics_response()
