from __future__ import annotations

from app.workers.celery_app import celery_app


@celery_app.task(name="agent_worker.health")
def health() -> dict:
    return {"worker": "agent_worker", "status": "ready"}
