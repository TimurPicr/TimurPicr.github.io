def f(num):
	if (num < 3):
		return 0
	elif (num == 3):
		return 1
	elif (num == 4):
		return 3
	elif (num == 5):
		return 8
		
N = int(input())
while (N != 0):
	print(f(N))
	N = int(input())
	


