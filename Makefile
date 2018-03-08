.PHONY: clean

svd_eye_1thread.out: ext.c
	MKL_NUM_THREADS=1 python svd_eye.py > $@

svd_eye.out: ext.c
	python svd_eye.py > $@

ext.c:
	python setup.py build_ext --inplace

clean:
	rm -rf ext.c ext.cpython* build svd_eye*.png svd_eye*.out

environment.yaml:
	conda install numpy scipy cython mkl gcc seaborn
	conda env export > $@
