from __future__ import annotations

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, TimestampMixin


class Project(TimestampMixin, Base):
    __tablename__ = "projects"
    name: Mapped[str] = mapped_column(String(255), index=True)
    description: Mapped[str] = mapped_column(String(2000), default="")
    owner_email: Mapped[str] = mapped_column(String(255), index=True)
    settings: Mapped[dict] = mapped_column(JSON, default=dict)
