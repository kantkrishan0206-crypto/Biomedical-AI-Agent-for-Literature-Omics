from __future__ import annotations


async def execute(payload: dict) -> dict:
    return {"tool": "pubmed_tool", "status": "complete", "payload": payload}
