from mylib import *
import os,sys
import numpy as np
import matplotlib.pyplot as plt
import math
import random

if __name__ == '__main__':
	DIR_PATH = sys.path[0] + '\\'

	# normal distribution vector file
	nvctr_file1 = DIR_PATH + 'normal_500_1.txt'
	nvctr_file2 = DIR_PATH + 'normal_500_2.txt'
	# uniform distribution vector file
	uvctr_file1 = DIR_PATH + 'uniform_500_1.txt'
	uvctr_file2 = DIR_PATH + 'uniform_500_2.txt'

	posi = random.randint(0,1000)

	if posi < 500:
		nvctr = fget_vctr(nvctr_file1, posi)
		uvctr = fget_vctr(uvctr_file1, posi)
	else:
		nvctr = fget_vctr(nvctr_file2, posi - 500)
		uvctr = fget_vctr(uvctr_file1, posi - 500)
	print("Normal distribution vector:")
	print(nvctr)
	print("Uniform distribution vector:")
	print(uvctr)

	ex,var = get_normal_param(nvctr)
	a, b = get_uniform_param(uvctr)

	print('Parameter of normal distribution:')
	print('expectation = ', end='')
	print(ex)
	print('variance = ', end='')
	print(var)
	print()
	print('Parameter of uniform distribution:')
	print('a = ', end='')
	print(a)
	print('b = ', end='')
	print(b)
