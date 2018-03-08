#!/usr/bin/env python3

from setuptools import setup, Extension
#import os

from Cython.Build import cythonize
import numpy

extensions = [
    Extension("ext",
    	  sources=["ext.pyx"],
    	  extra_compile_args=['-fopenmp'],
    	  extra_link_args=['-fopenmp'],
    	  include_dirs=[numpy.get_include()])]
extensions = cythonize(extensions)


setup(ext_modules=extensions)
