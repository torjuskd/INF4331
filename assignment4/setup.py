# setup.py: A simple script for installing the module 'my_unit_testing'
# To install use:
# sudo python3 setup.py install

import mandelbrot_3_setup
import mandelbrot
from distutils.core import setup
name='mandelbrot'
name2='mandelbrot_3'

setup(name=name,
      version='0.1',
      description='mandelbrot',
      py_modules=[name],       # modules to be installed
      scripts=[name + '.py', name2 + '.py'],  # programs to be installed
      )
