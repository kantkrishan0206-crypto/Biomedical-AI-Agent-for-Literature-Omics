from app.omics.visualization import umap_projection


def test_omics_contract():
    points = umap_projection(32)
    assert len(points) == 32
    assert {"x", "y", "cluster"}.issubset(points[0])
