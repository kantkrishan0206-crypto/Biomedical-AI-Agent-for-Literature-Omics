import pytest

from app.services.project_service import ProjectService


@pytest.mark.asyncio
async def test_projects_contract():
    project = await ProjectService().create({"name": "SMA Therapeutics"})
    assert project["status"] == "created"
    assert project["payload"]["name"] == "SMA Therapeutics"
