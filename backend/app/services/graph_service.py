from __future__ import annotations

import json
from pathlib import Path


class GraphService:
    def __init__(self, db=None, settings=None) -> None:
        self.db = db
        self.settings = settings

    async def snapshot(self) -> dict:
        path = Path("data/samples/sample_graph.json")
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
        return {"nodes": [], "edges": []}

    async def traverse(self, node_id: str, depth: int = 2) -> dict:
        graph = await self.snapshot()
        edges = [edge for edge in graph["edges"] if node_id in (edge["source"], edge["target"])]
        return {"start": node_id, "depth": depth, "edges": edges, "nodes": graph["nodes"]}
