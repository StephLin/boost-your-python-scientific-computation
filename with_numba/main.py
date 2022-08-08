import argparse
import time

import numpy as np

import lib


def main():
    print("Initializing ...")
    start = time.perf_counter()
    size = 30000001
    points = np.zeros((size, 3), dtype=float)
    points[:, 0] = np.arange(size, dtype=float)
    end = time.perf_counter()
    print("Initialization time:", end - start)

    computational_time = []
    print("Start computing ({} x 3) * 2 ...".format(size))
    for _ in range(3):
        start = time.perf_counter()
        result = lib.arc_length(points)
        end = time.perf_counter()
        computational_time.append(end - start)
    print("Complete.")
    print(
        "Expected:",
        size - 1,
        "Result:",
        result,
        "Time (init):",
        computational_time[0],
        "Time:",
        computational_time[1],
    )

    points = np.zeros((10000, 10000), dtype=float)
    points[0, 0] = 1.0

    print("Start computing (10000 x 10000) ...")
    start = time.perf_counter()
    result = lib.arc_length(points)
    end = time.perf_counter()
    print("Complete.")
    print("Expected:", 1, "Result:", result, "Time:", end - start)


if __name__ == "__main__":
    main()
