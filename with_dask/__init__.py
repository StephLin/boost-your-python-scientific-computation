from concurrent.futures import ThreadPoolExecutor

import dask
import dask.array as da

from .lib import arc_length

dask.config.set(pool=ThreadPoolExecutor(16))


def create_data(x: int, y: int):
    points = da.zeros((x, y), dtype=float)
    points[:, 0] = da.arange(x, dtype=float)
    return points
