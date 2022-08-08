import numba as nb
import numpy as np
from numba.pycc import CC

cc = CC("lib")


@cc.export("arc_length", "f8(f8[:,:])")
def arc_length(points: np.ndarray) -> float:
    """Compute the arc length of a discrete set of points (curve).

    Args:
        points (np.ndarray): A list of points.

    Returns:
        float: Arc length.
    """
    length = 0
    for i in range(points.shape[0] - 1):
        piecewice_length = np.sqrt(sum((points[i + 1] - points[i]) ** 2))
        length += piecewice_length
    return length


if __name__ == "__main__":
    cc.compile()
