from __future__ import annotations


async def execute(payload: dict) -> dict:
    return {"tool": "citation_tool", "status": "complete", "payload": payload}
