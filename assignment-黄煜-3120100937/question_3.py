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

	for i in range(10):
		posi = random.randint(0,1000)

		if posi < 500:
			nvctr.append(fget_vctr(nvctr_file1, posi))
			uvctr.append(fget_vctr(uvctr_file1, posi))
		else:
			nvctr.append(fget_vctr(nvctr_file2, posi - 500))
			uvctr.append(fget_vctr(uvctr_file1, posi - 500))

		plt.figure(1)
		plt.subplot(2,5,i+1)
		my_hist(nvctr[i], bucket_size = 20, flat_edge = True, title = 'normal vector'+str(i+1))

		plt.figure(2)
		plt.subplot(2,5,i+1)
		my_hist(uvctr[i], bucket_size = 20, flat_edge = True, title = 'uniform vector'+str(i+1))
	
	for i in range(10):
		ex,var = get_normal_param(nvctr[i])
		print('expectation = ',end='')
		print(ex,end='')
		print(' variance = ', end=''),
		print(var)

	for i in range(10):
		a,b = get_uniform_param(uvctr[i])
		print('a = ',end='')
		print(a,end='')
		print(' b = ', end=''),
		print(b)


	print(np.linalg.norm(nvctr[0]))

	plt.show()

	# Compute norm of all vectors of each data set
	
	
