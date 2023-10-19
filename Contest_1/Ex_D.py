a = input()
l =list(map(int, input().split()))
size = len(l)
m = l[:]

for i in range(size - 2, -1, -1):
	m[i] = max(l[i], m[i + 1])

cash = 0
for i in range(size):
	cash += m[i] - l[i]
print(cash)




		
			
			
