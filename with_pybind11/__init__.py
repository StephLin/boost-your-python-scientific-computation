import os.path as osp
import sys

import numpy as np

# pyright: reportMissingImports=false
sys.path.append(osp.join(osp.dirname(osp.abspath(__file__)), "build"))
from lib import arc_length

sys.path.pop()


def create_data(x: int, y: int):
    points = np.zeros((x, y), dtype=float)
    points[:, 0] = np.arange(x, dtype=float)
    return points
