from __future__ import annotations

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, TimestampMixin


class RegisteredModel(TimestampMixin, Base):
    __tablename__ = "registered_models"
    name: Mapped[str] = mapped_column(String(255), index=True)
    version: Mapped[str] = mapped_column(String(64), default="1.0.0")
    endpoint: Mapped[str] = mapped_column(String(1000), default="ollama")
    metadata_json: Mapped[dict] = mapped_column(JSON, default=dict)
    rollout_status: Mapped[str] = mapped_column(String(64), default="candidate")
