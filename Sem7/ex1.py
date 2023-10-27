class Vector():
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def __abs__():
		return (self.x**2 + self.y**2 + self.z**2)**0.5
		
	def __add__(self, v):
		return Vector(self.x + v.x, self.y + v.y, self.z + v.z)
	def __sub__(self, v):
		return Vector(self.x - v.x, self.y - v.y, self.z - v.z)
	
	
vec1 = Vector(1, 2, 3)
vec2 = Vector(3, 4, 5)
vec3 = vec1 + vec2
print(vec3.x, vec3.y, vec3.z)
