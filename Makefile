.PHONY: clean

out/svd_eye_1thread.out: ext.c
	mkdir -p $(@D)
	MKL_NUM_THREADS=1 python svd_eye.py > $@

out/svd_eye.out: ext.c
	mkdir -p $(@D)
	python svd_eye.py > $@

ext.c:
	python setup.py build_ext --inplace

clean:
	rm -rf ext.c ext.cpython* build out

environment.yaml:
	conda install numpy scipy cython mkl gcc seaborn
	conda env export > $@
