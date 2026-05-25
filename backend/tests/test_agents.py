import pytest

from app.services.agent_service import AgentService


@pytest.mark.asyncio
async def test_agents_contract():
    result = await AgentService().run("SMN2 evidence in SMA")
    assert result["status"] == "complete"
    assert result["citations"]
    assert len(result["trace"]) == 7
