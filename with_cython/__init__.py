# pyright: reportMissingImports=false
import numpy as np

from .lib import arc_length


def create_data(x: int, y: int):
    points = np.zeros((x, y), dtype=float)
    points[:, 0] = np.arange(x, dtype=float)
    return points
