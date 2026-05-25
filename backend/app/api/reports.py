from __future__ import annotations

from fastapi import APIRouter

from app.api.deps import CurrentClaims
from app.services.report_service import ReportService

router = APIRouter(prefix="/reports", tags=["reports"])


@router.post("/compile")
async def compile_report(payload: dict, claims: CurrentClaims):
    report = await ReportService().compile(payload)
    report["actor"] = claims["sub"]
    return report
