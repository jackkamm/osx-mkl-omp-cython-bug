cimport numpy as np
import numpy as np
import cython
from cython.parallel import prange

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def p_arange(int n):
    '''
    A useless function only for demonstration purposes
    '''
    cdef np.ndarray[np.int_t, ndim=1] ret = np.zeros(n)
    for i in range(n, schedule='guided', nogil=True):
        ret[i] = i
    return ret
