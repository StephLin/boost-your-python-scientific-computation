import dask.array as da


def arc_length(points, compute=True) -> float:
    """Compute the arc length of a discrete set of points (curve).

    Args:
        points (np.ndarray): A list of points.

    Returns:
        float: Arc length.
    """
    piecewice_length = da.linalg.norm(da.diff(points, axis=0), axis=1)
    return da.sum(piecewice_length).compute() if compute else da.sum(piecewice_length)
