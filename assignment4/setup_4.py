#!/usr/bin/env python3
# set up with:
# swig -python mandelbrot_4.i
# python3 setup_4.py build_ext --inplace

# Run with:
# ./mandelbrot_4_starter.py

"""
setup4.py file for SWIG mandelbrot_4
"""

from distutils.core import setup, Extension


example_module = Extension('_mandelbrot_4',
                           sources=['mandelbrot_4_wrap.c', 'mandelbrot_4.c'],
                           )

setup (name = 'example',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [example_module],
       py_modules = ["example"],
       )
