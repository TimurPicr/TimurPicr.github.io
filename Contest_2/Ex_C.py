import numpy as np
def f(T: int, coord):
	array = []
	lengths = []
	for i in range(len(coord) - 1):
		lengths.append(len(coord[i+1] - coord[i]))
	length = length / (T - 1)
	col = 0
	for i in range(len(lengths)):
		if col < sum(lengths[:i]):
			
