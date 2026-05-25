from __future__ import annotations

from app.workers.celery_app import celery_app


@celery_app.task(name="ingestion_worker.health")
def health() -> dict:
    return {"worker": "ingestion_worker", "status": "ready"}
