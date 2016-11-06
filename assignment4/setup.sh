#!/bin/bash
# Setup file for running setup-scripts
#"master" setup script for compiling/installing all the scripts

swig -python mandelbrot_4_swig.i
sudo python3 mandelbrot_4_setup.py build_ext --inplace
sudo python3 ./mandelbrot_3_setup.py build_ext --inplace
sudo python3 ./setup.py install
