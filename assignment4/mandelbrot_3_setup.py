#!/usr/bin/env python3
# file for easier compilation
# compile with:
# python3 setup_3.py build_ext --inplace

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "mandelbrot_3_cython",
    ext_modules = cythonize("*.pyx"),
)
