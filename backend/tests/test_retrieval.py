import pytest

from app.services.retrieval_service import RetrievalService


@pytest.mark.asyncio
async def test_retrieval_contract():
    result = await RetrievalService().search("SMN2 splicing")
    assert result["results"][0]["pmid"] == "34205212"
    assert result["metrics"]["citation_precision"] > 0.9
