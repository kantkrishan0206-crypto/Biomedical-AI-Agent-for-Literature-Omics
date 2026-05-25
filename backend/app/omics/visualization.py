from __future__ import annotations

import math


def umap_projection(rows: int = 240) -> list[dict]:
    points = []
    for index in range(rows):
        cluster = index % 9
        angle = index * 0.37
        radius = 4 + cluster * 0.5 + math.sin(index) * 0.4
        points.append({"x": round(math.cos(angle) * radius, 3), "y": round(math.sin(angle) * radius, 3), "cluster": cluster})
    return points
