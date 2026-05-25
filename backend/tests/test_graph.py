import pytest

from app.services.graph_service import GraphService


@pytest.mark.asyncio
async def test_graph_contract():
    graph = await GraphService().snapshot()
    assert graph["nodes"]
    traversal = await GraphService().traverse("gene:SMN2")
    assert traversal["edges"]
