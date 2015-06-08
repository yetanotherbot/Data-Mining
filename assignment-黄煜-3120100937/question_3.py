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

	nvctr = []
	uvctr = []

	plt.figure(1)
	for i in range(10):
		posi = random.randint(0,1000)

		if posi < 500:
			nvctr.append(fget_vctr(nvctr_file1, posi))
		else:
			nvctr.append(fget_vctr(nvctr_file2, posi - 500))

		ex,var = get_normal_param(nvctr[i])
		print('expectation = ',end='')
		print(ex,end='')
		print(' variance = ', end=''),
		print(var)

		plt.subplot(2,5,i+1)
		my_hist(nvctr[i], bucket_size = 20, flat_edge = True, title = 'normal'+str(i+1))
	
	plt.show()

	plt.figure(2)
	for i in range(10):
		posi = random.randint(0,1000)

		if posi < 500:
			uvctr.append(fget_vctr(uvctr_file1, posi))
		else:
			uvctr.append(fget_vctr(uvctr_file1, posi - 500))

		a,b = get_uniform_param(uvctr[i])
		print('a = ',end='')
		print(a,end='')
		print(' b = ', end=''),
		print(b)

		plt.subplot(2,5,i+1)
		my_hist(uvctr[i], bucket_size = 20, flat_edge = True, title = 'uniform'+str(i+1))
	
	plt.show()

	nnorm = []
	unorm = []

	nmtrx = fget_mtrx(nvctr_file1) + fget_mtrx(nvctr_file2)
	umtrx = fget_mtrx(uvctr_file1) + fget_mtrx(uvctr_file2)

	for vctr in nmtrx:
		nnorm.append(np.linalg.norm(np.array(vctr),2))

	for vctr in umtrx:
		unorm.append(np.linalg.norm(np.array(vctr),2))

	ex,var = get_normal_param(nnorm)
	print('expectation = ',end='')
	print(ex,end='')
	print(' variance = ', end=''),
	print(var)
	plt.figure(3)
	my_hist(nnorm, bucket_size = 100, flat_edge = True, title = 'histrogram of norm distribution of normal dataset')
	plt.show()

	a,b = get_uniform_param(unorm)
	print('a = ',end='')
	print(a,end='')
	print(' b = ', end=''),
	print(b)
	plt.figure(4)
	my_hist(unorm, bucket_size = 100, flat_edge = True, title = 'histrogram of norm distribution of uniform dataset')
	plt.show()
	