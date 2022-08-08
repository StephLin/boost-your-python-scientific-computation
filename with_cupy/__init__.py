import cupy as cp

from .lib import arc_length


def create_data(x: int, y: int):
    points = cp.zeros((x, y), dtype=float)
    points[:, 0] = cp.arange(x, dtype=float)
    return points
