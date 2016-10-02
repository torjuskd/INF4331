#!/usr/bin/env python3
# file for easier compilation
# compile with:
# python setup.py build_ext --inplace

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "apply",
    ext_modules = cythonize("*.pyx"),
)
