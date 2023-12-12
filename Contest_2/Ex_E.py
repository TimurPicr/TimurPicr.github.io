class Matrix():
	name = ''
	left = 0
	right = 0
	def __init__(self, name, left, right):
		self.name = name
		self.left = left
		self.right = right
	def __str__(self):
		return "Matrix: (" + str(self.name) + " " + str(self.left) + " " + str(self.right) + ")"
	def __add__(self, other):
		if (self.right != other.left):
			return 0
		else:
			return Matrix(self.name + other.name, self.left, other.right)

matrixes = []

N = int(input())
for i in range(N):
	abuba = list(map(str, input().split()))
	matrixes.append(Matrix(abuba[0], int(abuba[1]), int(abuba[2])))
	
abuba = str(input())
while (abuba != '0'):
	if (len(abuba) == 1):
		print(0)
		abuba = str(input())
	else:
	
		s = abuba
		var = []
		for i in s:
			for j in matrixes:
				if (i == j.name):
					var.append(Matrix(j.name, j.left, j.right))
			

		array = []
		points = []
		array.append(var)
		points.append(0)
		for _ in range(len(s)-1):
			for i in range(len(array)): 
				for j in range(len(array[i])-1):
					if (array[i][j] + array[i][j+1] != 0):
						banana = []
						for k in array[i]:
							if (k == array[i][j]):
								banana.append(array[i][j] + array[i][j+1])
							elif (k != array[i][j+1]):
								banana.append(k)
					
						array.append(banana)		
						points.append(points[i] + array[i][j].left * array[i][j].right * array[i][j+1].right)
					else: 
						continue
				array[i] = []
				points[i] = 1000000
		flag = False
		for i in points:
			if (i != 1000000):
				flag = True
				break
		if (flag):
			print(min(points))
		else:
			print("error")
		abuba = str(input())

			



