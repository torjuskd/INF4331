#!/usr/bin/env python3
# file for easier compilation
# compile with:
# python3 mandelbrot_3_setup.py build_ext --inplace

from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension


extensions = [
    Extension("mandelbrot_3_cython", ["mandelbrot_3_files/mandelbrot_3_cython.pyx"])
    ]

setup(
    ext_modules = cythonize(extensions)
)

