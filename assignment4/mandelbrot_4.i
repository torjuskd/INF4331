/* File: mandelbrot_4.i */
%module mandelbrot_4

%{
#define SWIG_FILE_WITH_INIT
#include "mandelbrot_4.h"
%}

int mandelbrot_4(double c_real, double c_imag, int stepLimit);
