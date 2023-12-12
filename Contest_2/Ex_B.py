U = [1, 2, 3] + [0]*28
P = [1, 2, 4] + [0]*28
for i in range(3, 31):
	P[i] = P[i-1] + U[i-1]
	U[i] = P[i-1] + P[i-2]
print(U)
print(P)
buba = int(input())
while (buba != 0):
	print(2**buba - U[buba-1] - P[buba-1])
	buba = int(input())

	


