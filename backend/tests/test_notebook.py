from app.notebook.exports import process


def test_notebook_contract():
    result = process({"title": "SMA lab book"})
    assert result["notebook_versioned"] is True
