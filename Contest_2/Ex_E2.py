class Matrix():
	name = ''
	left = 0
	right = 0
	def __init__(self, name, left, right):
		self.name = name
		self.left = left
		self.right = right
	#def __str__(self):
		#return "Matrix: (" + str(self.name) + " " + str(self.left) + " " + str(self.right) + ")"
	def __add__(self, other):
		if (self.right != other.left):
			return 0
		else:
			return Matrix(self.name + other.name, self.left, other.right)
			
matrix = [Matrix('A', 50, 10), Matrix('B', 10, 20), Matrix('C', 20, 5), Matrix('D', 30, 35), Matrix('E', 35, 10)]
						
names = [matrix] #Активные комбинации матриц

points = [0] #Сколько было потрачено поинтов
#for _ in range(len(matrix)): #Сколько будем укорачивать матрицу
for i in range(len(names)): # Для каждого [A, B, C, D...]
		
	for j in range(len(names[i])):
		for k in range(len(names[i])):
			if (names[i][j] + names[i][k] != 0):
				for t in range
				names.append([names[i][j] + names[i][k]])
				points.append(points[i] + names[i][j].left * names[i][j].right * names[i][k].right)
				#del names[i]
				#del points[i]
				
print(names)
print(points)
