import numpy as np


# pythran export arc_length(float64[:, :])
def arc_length(points):
    """Compute the arc length of a discrete set of points (curve).

    Args:
        points (float64[:, :]): A list of points.

    Returns:
        float: Arc length.
    """
    length = 0

    # omp parallel for reduction(+:length)
    for i in range(points.shape[0] - 1):
        length += np.linalg.norm(points[i + 1] - points[i])

    return length
