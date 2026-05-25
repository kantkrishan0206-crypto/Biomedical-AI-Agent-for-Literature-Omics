from __future__ import annotations

import asyncio
import json

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.services.telemetry_service import TelemetryService

router = APIRouter(prefix="/telemetry", tags=["telemetry"])


@router.get("")
async def telemetry():
    return await TelemetryService().summary()


@router.get("/stream")
async def telemetry_stream():
    async def events():
        for _ in range(20):
            yield f"data: {json.dumps(await TelemetryService().summary())}\n\n"
            await asyncio.sleep(1)
    return StreamingResponse(events(), media_type="text/event-stream")
