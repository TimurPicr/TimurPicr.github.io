inp = input().split(' ')
a = int(inp[0])
b = int(inp[1])

x = 0
while ((a+x)%b!=0 or (b+x)%a!=0):
	x += 1
print(x)

