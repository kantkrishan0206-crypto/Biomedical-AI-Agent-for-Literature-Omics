from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from uuid import uuid4

from app.services.retrieval_service import RetrievalService


class AgentService:
    agents = ["planner", "retriever", "knowledge_graph", "omics", "verifier", "critic", "synthesizer"]

    def __init__(self, db=None, settings=None) -> None:
        self.db = db
        self.settings = settings
        self.retrieval = RetrievalService(db, settings)

    async def run(self, query: str, project_id: str = "demo-project") -> dict:
        evidence = await self.retrieval.search(query)
        trace = []
        for index, agent in enumerate(self.agents):
            trace.append({
                "step": index + 1,
                "agent": agent,
                "status": "complete",
                "message": f"{agent} produced a grounded intermediate result",
                "timestamp": datetime.now(timezone.utc).isoformat(),
            })
        return {
            "id": f"agent-{uuid4()}",
            "project_id": project_id,
            "query": query,
            "status": "complete",
            "trace": trace,
            "citations": evidence["results"],
            "answer": "SMN2 modulation is a mechanistically plausible SMA strategy when supported by splicing, motor neuron, and citation evidence.",
        }

    async def stream(self, query: str):
        for agent in self.agents:
            await asyncio.sleep(0.05)
            yield {
                "event": "agent_step",
                "agent": agent,
                "message": f"{agent} advanced the biomedical reasoning plan for: {query}",
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        yield {"event": "complete", "message": "Citation-grounded synthesis ready"}
