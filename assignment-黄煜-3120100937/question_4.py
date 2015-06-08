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

	vctr = fget_vctr(nvctr_file1, 1)
	y = my_DCT_compression(vctr)
	print(y)
	x = range(0,100)
	plt.plot(x,y)
	plt.show()