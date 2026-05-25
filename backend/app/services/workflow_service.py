from __future__ import annotations

from uuid import uuid4

from app.workflows.dag_engine import ScientificDAGEngine


class WorkflowService:
    def __init__(self, db=None, settings=None) -> None:
        self.db = db
        self.settings = settings
        self.engine = ScientificDAGEngine()

    async def compile_and_run(self, name: str, project_id: str = "demo-project") -> dict:
        dag = {
            "nodes": [
                {"id": "ingest", "kind": "retrieval"},
                {"id": "index", "kind": "qdrant"},
                {"id": "reason", "kind": "agent"},
                {"id": "report", "kind": "report"},
            ],
            "edges": [["ingest", "index"], ["index", "reason"], ["reason", "report"]],
        }
        result = await self.engine.execute(dag)
        return {"id": f"workflow-{uuid4()}", "name": name, "project_id": project_id, "status": "complete", "dag": dag, "result": result}
