/* File: mandelbrot_4.c */

#include "mandelbrot_4.h"
#include <math.h>
double sqrt (double x );

int mandelbrot_4(double c_real, double c_imag, int stepLimit){
double z_real = 0.0;
double z_imag = 0.0;
double z_real_tmp = 0.0;
double z_imag_tmp = 0.0;

int steps = 0;

for(steps=0; steps < stepLimit; steps++){
if (sqrt(z_real*z_real+z_imag*z_imag) > 2.0) return steps;

z_real_tmp = z_real * z_real - z_imag * z_imag + c_real;
z_imag_tmp = z_imag * z_real + z_real * z_imag + c_imag;
z_real = z_real_tmp;
z_imag = z_imag_tmp;
}
return -1;
}
