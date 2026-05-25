from __future__ import annotations


def execute(graph: dict) -> dict:
    return {"component": "sync", "nodes": len(graph.get("nodes", [])), "edges": len(graph.get("edges", []))}
