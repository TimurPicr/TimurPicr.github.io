class Tree():
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
	
def polish(s):
	ints = []
	ops = []
	a = ''
	for i in s:
		if (i in '1234567890'):
			a += i
		else:
			ints.append(a)
			a = ''
			ints.append(i)
			
	
