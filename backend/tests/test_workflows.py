import pytest

from app.services.workflow_service import WorkflowService


@pytest.mark.asyncio
async def test_workflows_contract():
    workflow = await WorkflowService().compile_and_run("SMA Hypothesis Generation")
    assert workflow["status"] == "complete"
    assert workflow["result"]["replayable"] is True
