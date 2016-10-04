/* File: mandelbrot_4_swig.i */
%module mandelbrot_4_swig

%{
#define SWIG_FILE_WITH_INIT
#include "mandelbrot_4_swig.h"
%}

int mandelbrot_4(double c_real, double c_imag, int stepLimit);
