import time

import lib


def main():
    print("Initializing ...")
    start = time.perf_counter()
    size = 30000001
    points = [[float(i), 0, 0] for i in range(size)]
    end = time.perf_counter()
    print("Initialization time:", end - start)

    print("Start computing ({} x 3) ...".format(size))
    start = time.perf_counter()
    result = lib.arc_length(points)
    end = time.perf_counter()
    print("Complete.")
    print("Expected:", size - 1, "Result:", result, "Time:", end - start)

    points = [[0.0 for _ in range(10000)] for _ in range(10000)]
    points[0][0] = 1.0

    print("Start computing (10000 x 10000) ...")
    start = time.perf_counter()
    result = lib.arc_length(points)
    end = time.perf_counter()
    print("Complete.")
    print("Expected:", 1, "Result:", result, "Time:", end - start)


if __name__ == "__main__":
    main()
