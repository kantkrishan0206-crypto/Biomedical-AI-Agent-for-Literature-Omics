from __future__ import annotations

from fastapi import APIRouter

from app.services.graph_service import GraphService

router = APIRouter(prefix="/knowledge-graph", tags=["knowledge-graph"])


@router.get("")
async def graph():
    return await GraphService().snapshot()


@router.get("/traverse/{node_id}")
async def traverse(node_id: str, depth: int = 2):
    return await GraphService().traverse(node_id, depth)
