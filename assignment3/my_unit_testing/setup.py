# setup.py: A simple script for installing the module 'my_unit_testing'
# To install use:
# sudo python3 setup.py install

from distutils.core import setup
name='my_unit_testing'

setup(name=name,
      version='0.1',
      description='A simple tool for making unit tests easier to make',
      py_modules=[name],       # modules to be installed
      scripts=[name + '.py'],  # programs to be installed
      )
