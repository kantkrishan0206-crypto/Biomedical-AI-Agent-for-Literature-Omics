from app.provenance.manifests import build


def test_provenance_contract():
    result = build({"sha256": "abc", "source": "user_upload"})
    assert result["provenance_attached"] is True
