from __future__ import annotations

from typing import Annotated

from fastapi import Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings, get_settings
from app.core.security import decode_access_token
from app.db.session import get_session

DbSession = Annotated[AsyncSession, Depends(get_session)]
SettingsDep = Annotated[Settings, Depends(get_settings)]


async def current_claims(
    settings: SettingsDep,
    authorization: str | None = Header(default=None),
) -> dict:
    if settings.single_user_dev_mode and not authorization:
        return {"sub": settings.first_admin_email, "role": "admin"}
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")
    return decode_access_token(authorization.split(" ", 1)[1], settings.jwt_secret)


CurrentClaims = Annotated[dict, Depends(current_claims)]
