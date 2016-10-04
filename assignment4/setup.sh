#!/bin/bash
# Setup file for running setup-scripts

python3 ./mandelbrot_3_setup.py build_ext --inplace && sudo python3 ./setup.py install
