from __future__ import annotations

from fastapi import APIRouter

from app.api.deps import CurrentClaims, DbSession, SettingsDep
from app.services.experiment_service import ExperimentService

router = APIRouter(prefix="/experiments", tags=["experiments"])


@router.get("")
async def list_items(claims: CurrentClaims, db: DbSession, settings: SettingsDep, project_id: str | None = None):
    return {"actor": claims["sub"], "items": await ExperimentService(db, settings).list(project_id)}


@router.post("")
async def create_item(payload: dict, claims: CurrentClaims, db: DbSession, settings: SettingsDep):
    payload.setdefault("actor", claims["sub"])
    return await ExperimentService(db, settings).create(payload)
