from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings
from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User


class AuthService:
    def __init__(self, db: AsyncSession, settings: Settings) -> None:
        self.db = db
        self.settings = settings

    async def signup(self, email: str, password: str, full_name: str = "") -> User:
        existing = await self.db.scalar(select(User).where(User.email == email))
        if existing:
            return existing
        role = "admin" if email == self.settings.first_admin_email else "researcher"
        user = User(email=email, full_name=full_name, password_hash=hash_password(password), role=role)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def login(self, email: str, password: str) -> tuple[str, User]:
        user = await self.db.scalar(select(User).where(User.email == email))
        if not user:
            user = await self.signup(email, password, email.split("@")[0])
        if not verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials")
        token = create_access_token(user.email, self.settings.jwt_secret, user.role)
        return token, user
