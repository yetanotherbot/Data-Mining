from mylib import *
import os,sys
import numpy as np
import matplotlib.pyplot as plt
import math
import random


if __name__ == '__main__':

	DIR_PATH = sys.path[0] + '\\'

	# normal distribution vector file
	nvtr_file1 = DIR_PATH + 'normal_500_1.txt'
	nvtr_file2 = DIR_PATH + 'normal_500_2.txt'
	# uniform distribution vector file
	uvtr_file1 = DIR_PATH + 'uniform_500_1.txt'
	uvtr_file2 = DIR_PATH + 'uniform_500_2.txt'

	posi = random.randint(0,1000)

	if posi < 500:
		vctr = fget_vctr(nvtr_file1, posi)
	else:
		vctr = fget_vctr(nvtr_file2, posi - 500)
	print(vctr)

	my_hist(vctr, bucket_size = 20, flat_edge = True)
	plt.show()


