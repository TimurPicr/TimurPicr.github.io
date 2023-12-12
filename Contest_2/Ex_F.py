def g(n):
	if (n == 0):
		return [0]
	else:
		array = []
		for i in range(len(str(n))):
			array.append(int(''.join(map(str, str(n)[:i] + str(n)[i+1:]))))
		return max(array)
	
def f(num, l):
	for i in range(l):
		num = g(num)
	return num
	
banana = list(map(int, input().split()))
while (banana != [0, 0]):
	l = banana[1]
	num = int(input())
	print(f(num, l))
	banana = list(map(int, input().split()))	

	
		

			
	
	
	
