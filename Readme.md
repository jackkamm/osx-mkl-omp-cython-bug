This is a minimal example for reproducing a bug in MKL, Cython, and OpenMP on OSX.

To build the Cython module, do
```
make ext.c
```
This will also create the `.so` file that can then be imported into Python. Then run `svd_eye.py` to reproduce the error.
