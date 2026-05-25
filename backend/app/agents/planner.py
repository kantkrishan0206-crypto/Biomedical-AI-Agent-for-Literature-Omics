from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PlannerAgentResult:
    status: str
    summary: str
    confidence: float = 0.85


class PlannerAgent:
    """Decomposes biomedical questions into reproducible scientific plans."""

    async def run(self, payload: dict) -> PlannerAgentResult:
        return PlannerAgentResult(status="complete", summary=f"Decomposes biomedical questions into reproducible scientific plans: {payload}")
