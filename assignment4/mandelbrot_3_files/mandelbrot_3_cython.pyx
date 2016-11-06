import cython
cdef extern from "math.h":
    double abs(double x)

cdef extern from "math.h":
    double sqrt(double x)

cpdef int mandelbrot(double c_real, double c_imag, int stepLimit):
    cdef double z_real = 0.0
    cdef double z_imag = 0.0
    cdef double z_real_tmp = 0.0
    cdef double z_imag_tmp = 0.0

    cdef int steps = 0
    for steps in range(stepLimit):
        if sqrt(z_real*z_real+z_imag*z_imag) > 2.0:
            return steps
        z_real_tmp = z_real * z_real - z_imag * z_imag + c_real
        z_imag_tmp = z_imag * z_real + z_real * z_imag + c_imag
        z_real = z_real_tmp
        z_imag = z_imag_tmp
    return -1

