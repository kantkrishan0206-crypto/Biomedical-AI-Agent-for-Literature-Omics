from __future__ import annotations

import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse

from app.api.deps import CurrentClaims, DbSession, SettingsDep
from app.services.agent_service import AgentService

router = APIRouter(prefix="/agents", tags=["agents"])


@router.post("/run")
async def run_agent(payload: dict, claims: CurrentClaims, db: DbSession, settings: SettingsDep):
    return await AgentService(db, settings).run(payload.get("query", "What drives SMA pathogenesis?"), payload.get("project_id", "demo-project"))


@router.get("/stream")
async def stream_agent(query: str = "SMN2 therapeutic evidence"):
    service = AgentService()

    async def events():
        async for item in service.stream(query):
            yield f"data: {json.dumps(item)}\n\n"

    return StreamingResponse(events(), media_type="text/event-stream")


@router.websocket("/ws")
async def websocket_agent(websocket: WebSocket):
    await websocket.accept()
    service = AgentService()
    try:
        query = "live biomedical agent run"
        async for item in service.stream(query):
            await websocket.send_json(item)
        await websocket.close()
    except WebSocketDisconnect:
        return
