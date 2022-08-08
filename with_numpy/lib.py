import numpy as np


def arc_length(points: np.ndarray) -> float:
    """Compute the arc length of a discrete set of points (curve).

    Args:
        points (np.ndarray): A list of points.

    Returns:
        float: Arc length.
    """
    piecewice_length = np.linalg.norm(np.diff(points, axis=0), axis=1)
    return np.sum(piecewice_length)
