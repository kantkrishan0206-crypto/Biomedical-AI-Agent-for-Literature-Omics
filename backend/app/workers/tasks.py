from __future__ import annotations

from app.workers.celery_app import celery_app


@celery_app.task(name="tasks.health")
def health() -> dict:
    return {"worker": "tasks", "status": "ready"}
