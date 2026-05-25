from __future__ import annotations

from celery import Celery

from app.core.config import get_settings

settings = get_settings()
celery_app = Celery("biomedical_ai", broker=settings.redis_url, backend=settings.redis_url)
celery_app.conf.task_routes = {
    "ingestion.*": {"queue": "ingestion"},
    "workflow.*": {"queue": "workflow"},
    "agent.*": {"queue": "agent"},
}
