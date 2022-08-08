from typing import Union

import cupy as cp
import numpy as np


def arc_length(points: Union[cp.ndarray, np.ndarray], optimized: bool = True) -> float:
    """Compute the arc length of a discrete set of points (curve).

    Args:
        points (cp.ndarray): A list of points.

    Returns:
        float: Arc length.
    """
    xp = cp.get_array_module(points)
    if optimized:
        piecewice_length = xp.linalg.norm(xp.diff(points, axis=0), axis=1)
        return xp.sum(piecewice_length)
    else:
        length = 0
        for i in range(len(points) - 1):
            piecewice_length = xp.sum((points[i + 1] - points[i]) ** 2) ** 0.5
            length += piecewice_length
        return length
