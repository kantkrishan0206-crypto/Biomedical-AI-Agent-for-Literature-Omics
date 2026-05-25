from __future__ import annotations

from fastapi import APIRouter

from app.api.deps import CurrentClaims, DbSession, SettingsDep
from app.services.retrieval_service import RetrievalService

router = APIRouter(prefix="/retrieval", tags=["retrieval"])


@router.post("/search")
async def search(payload: dict, claims: CurrentClaims, db: DbSession, settings: SettingsDep):
    result = await RetrievalService(db, settings).search(payload.get("query", "SMN2 spinal muscular atrophy"), payload.get("k", 5))
    result["actor"] = claims["sub"]
    return result
