import time

# import numpy as np
import dask.array as da

import lib


def main():
    print("Initializing ...")
    start = time.perf_counter()
    size = 30000001
    points = da.zeros((size, 3), dtype=float)
    points[:, 0] = da.arange(size, dtype=float)
    end = time.perf_counter()
    print("Initialization time:", end - start)

    print("Start computing ({} x 3) ...".format(size))
    start = time.perf_counter()
    result = lib.arc_length(points)
    end = time.perf_counter()
    print("Complete.")
    print("Expected:", size - 1, "Result:", result, "Time:", end - start)

    points = da.zeros((10000, 10000), dtype=float)
    points[0, 0] = 1.0

    print("Start computing (10000 x 10000) ...")
    start = time.perf_counter()
    result = lib.arc_length(points)
    end = time.perf_counter()
    print("Complete.")
    print("Expected:", 1, "Result:", result, "Time:", end - start)

if __name__ == "__main__":
    main()
