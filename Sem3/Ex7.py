N = 5
M = 6
m = [[1, 2, 5], [6, 0, 2], [0, 1, 10]]

def det(matrix):
	print('m = ', matrix)
	if (len(matrix) == 2):
		return float(matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
	else:
		a = 0
		for i in range(len(matrix)):
			mat = [[]]*len(matrix)
			print(mat)
			for y in range(len(matrix)):			
				for x in range(len(matrix)):
					b = matrix[y][x]
					mat[y].append(b)
			print("asdfasfasfaasasfasdf")
			del mat[0]
			for j in range(0, len(matrix)-1):
				del mat[j][i]
			print(matrix)
			if (i % 2 == 0):
				print("ex 1")
				a = a + (matrix[0][i]) * float(det(mat))
				
				print('a = ', a)
				
			else:
				print("ex 2")
				a = a - (matrix[0][i]) * float(det(mat))
				
				print('b = ', a)
		return a
print(det(m))
			
