from libc.math cimport sqrt
cimport cython


@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
cpdef arc_length(double[:, :] points):
    """Compute the arc length of a discrete set of points (curve).

    Args:
        points (double[:, :]): A list of points.

    Returns:
        double: Arc length.
    """
    cdef double length = 0
    cdef double square_diff = 0
    cdef int r = points.shape[0]
    cdef int c = points.shape[1]
    for i in range(r - 1):
        square_diff = 0
        for j in range(c):
            square_diff += (points[i+1, j] - points[i, j])**2
        length += sqrt(square_diff)

    return length