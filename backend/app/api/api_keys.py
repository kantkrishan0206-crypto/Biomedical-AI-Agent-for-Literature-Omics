from __future__ import annotations

from fastapi import APIRouter

from app.api.deps import CurrentClaims, DbSession, SettingsDep
from app.services.usage_tracker import UsageTracker

router = APIRouter(prefix="/api-keys", tags=["api-keys"])


@router.get("")
async def list_items(claims: CurrentClaims, db: DbSession, settings: SettingsDep, project_id: str | None = None):
    return {"actor": claims["sub"], "items": await UsageTracker(db, settings).list(project_id)}


@router.post("")
async def create_item(payload: dict, claims: CurrentClaims, db: DbSession, settings: SettingsDep):
    payload.setdefault("actor", claims["sub"])
    return await UsageTracker(db, settings).create(payload)
