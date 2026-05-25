from __future__ import annotations

from fastapi import APIRouter

from app.api.deps import CurrentClaims, DbSession, SettingsDep
from app.services.subscription_service import SubscriptionService

router = APIRouter(prefix="/quotas", tags=["quotas"])


@router.get("")
async def list_items(claims: CurrentClaims, db: DbSession, settings: SettingsDep, project_id: str | None = None):
    return {"actor": claims["sub"], "items": await SubscriptionService(db, settings).list(project_id)}


@router.post("")
async def create_item(payload: dict, claims: CurrentClaims, db: DbSession, settings: SettingsDep):
    payload.setdefault("actor", claims["sub"])
    return await SubscriptionService(db, settings).create(payload)
