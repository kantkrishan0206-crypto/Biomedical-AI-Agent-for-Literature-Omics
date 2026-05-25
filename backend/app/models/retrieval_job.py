from __future__ import annotations

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, TimestampMixin


class RetrievalJob(TimestampMixin, Base):
    __tablename__ = "retrieval_jobs"
    project_id: Mapped[str] = mapped_column(String(64), index=True)
    query: Mapped[str] = mapped_column(String(1000))
    status: Mapped[str] = mapped_column(String(64), default="complete")
    results: Mapped[list] = mapped_column(JSON, default=list)
