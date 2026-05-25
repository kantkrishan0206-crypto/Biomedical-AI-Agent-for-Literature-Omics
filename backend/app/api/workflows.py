from __future__ import annotations

from fastapi import APIRouter

from app.api.deps import CurrentClaims, DbSession, SettingsDep
from app.services.workflow_service import WorkflowService

router = APIRouter(prefix="/workflows", tags=["workflows"])


@router.post("/run")
async def run_workflow(payload: dict, claims: CurrentClaims, db: DbSession, settings: SettingsDep):
    return await WorkflowService(db, settings).compile_and_run(payload.get("name", "SMA Hypothesis Generation"), payload.get("project_id", "demo-project"))


@router.post("/{workflow_id}/cancel")
async def cancel_workflow(workflow_id: str, claims: CurrentClaims):
    return {"id": workflow_id, "status": "cancelling", "actor": claims["sub"]}
