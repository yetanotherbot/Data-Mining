from mylib import *
import os,sys
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from time import time

if __name__ == '__main__':
	DIR_PATH = sys.path[0] + '\\'

	# normal distribution vector file
	nvctr_file1 = DIR_PATH + 'normal_500_1.txt'
	nvctr_file2 = DIR_PATH + 'normal_500_2.txt'
	# uniform distribution vector file
	uvctr_file1 = DIR_PATH + 'uniform_500_1.txt'
	uvctr_file2 = DIR_PATH + 'uniform_500_2.txt'

	# normal distribution matrix
	nmtrx = fget_mtrx(nvctr_file1) + fget_mtrx(nvctr_file2)
	# uniform distribution matrix
	umtrx = fget_mtrx(uvctr_file1) + fget_mtrx(uvctr_file2)

	# plist is list the numbers of dimensions after DCT compression
	# nplist is for normal distribution data set
	# uplist is for uniform distribution data set
	nplist = []
	uplist = []
	for vector in nmtrx:
		u, p = my_DCT_compression(vector, 0.01)
		nplist.append(p)

	for vector in umtrx:
		u, p = my_DCT_compression(vector, 0.01)
		uplist.append(p)

	# draw histogram
	plt.figure(1)
	plt.subplot(2,1,1)
	my_hist(nplist, bucket_size = 1, flat_edge = False, title = "For normal distribution data set")
	plt.subplot(2,1,2)
	my_hist(uplist, bucket_size = 1, flat_edge = False, title = "For uniform distribution data set")
	plt.show()
	
	