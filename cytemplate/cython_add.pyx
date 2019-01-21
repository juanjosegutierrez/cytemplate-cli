cpdef int cython_add(int x):
    cdef int result = 0
    cdef int i
    for i in range(x):
        result += i
    return result
