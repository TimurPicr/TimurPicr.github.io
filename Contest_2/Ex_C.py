class Vector():
	x = 0.0
	y = 0.0
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)
	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)
	def __mul__(self, num):
		return Vector(self.x * num, self.y * num)
	def size(self):
		return (self.x**2 + self.y**2)**0.5

def f(T, V):

	L = 0
	for i in range(1, len(V)):
		L += (V[i] - V[i-1]).size()
	coord = [0]
	for i in range(1, len(V)):
		coord.append((V[i]-V[i-1]).size() + coord[i-1])
		
	tree_coord = [0]
	for i in range(T-1):
		tree_coord.append(tree_coord[i] + L/float(T-1))
	
	ans = []
	for i in tree_coord:
		for j in range(len(coord)-1):
			if (coord[j] <= i <= coord[j+1]):
				l = i - coord[j]
				ans.append(V[j] + (V[j+1]-V[j])*(l/((V[j+1]-V[j]).size())))
	for i in ans:
		print("{:.2f}".format(i.x), "{:.2f}".format(i.y))

N = int(input())
for i in range(N):
	V = []
	buba = list(map(int, input().split()))
	K = buba[0]
	T = buba[1]
	for j in range(K):
		abuba = list(map(float, input().split()))
		V.append(Vector(abuba[0], abuba[1]))
	print("Road #{}:".format(i+1))
	f(T, V)




			
