#!/usr/bin/env python3
# set up with:
# swig -python mandelbrot_4_swig.i
# python3 mandelbrot_4_setup.py build_ext --inplace

# Run with:
# ./mandelbrot_4.py

"""
setup4.py file for SWIG mandelbrot_4
"""

from distutils.core import setup, Extension


example_module = Extension('_mandelbrot_4_swig',
                           sources=['mandelbrot_4_swig_wrap.c', 'mandelbrot_4_swig.c'],
                           )

setup (name = 'example',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [example_module],
       py_modules = ["example"],
       )
