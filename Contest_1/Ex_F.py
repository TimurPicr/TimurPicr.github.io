papaia = input().split(' ')
n = int(papaia[0])
k = int(papaia[1])
array = list(map(int, input().split(" ")))
s = set()
for i in range(1, 2**n+1):
	if(i^k in range(1, 2**n+1)):
		s.add(array[i] + array[(i^k)])
print(max(s))
