from typing import List, Tuple


def arc_length(points: List[List[float]]) -> float:
    """Compute the arc length of a discrete set of points (curve).

    Args:
        points (List[List[float]]): A list of points.

    Returns:
        float: Arc length.
    """
    length = 0
    for i in range(len(points) - 1):
        square_diff = [(j - k) ** 2 for j, k in zip(points[i + 1], points[i])]
        length += sum(square_diff) ** 0.5

    return length
