import numba as nb
import numpy as np


@nb.njit(parallel=True)
def arc_length(points: np.ndarray) -> float:
    """Compute the arc length of a discrete set of points (curve).

    Args:
        points (np.ndarray): A list of points.

    Returns:
        float: Arc length.
    """
    length = 0
    for i in nb.prange(points.shape[0] - 1):
        piecewice_length = np.sqrt(np.sum((points[i + 1] - points[i]) ** 2))
        length += piecewice_length
    return length
