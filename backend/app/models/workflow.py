from __future__ import annotations

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, TimestampMixin


class WorkflowRun(TimestampMixin, Base):
    __tablename__ = "workflow_runs"
    project_id: Mapped[str] = mapped_column(String(64), index=True)
    name: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(64), default="queued")
    dag: Mapped[dict] = mapped_column(JSON, default=dict)
    checkpoints: Mapped[dict] = mapped_column(JSON, default=dict)
