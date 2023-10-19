nachos = input().split(' ')
n = int(nachos[0])
m = int(nachos[1])

def john(n=n, m=m):
	if(n%2==0 or m%2==0):
		return 0
#	elif(n==1 and m==1):
#		return 1
	else:
		return 1 + 4 * john((n-1)/2, (m-1)/2)
print(john())
