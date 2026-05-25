from __future__ import annotations

from app.workers.celery_app import celery_app


@celery_app.task(name="workflow_worker.health")
def health() -> dict:
    return {"worker": "workflow_worker", "status": "ready"}
