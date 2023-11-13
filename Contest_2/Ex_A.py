N = int(input())
l = list()
asymp = 0.0
flag = True
for i in range(N):
	m = list(map(float, input().split()))
	l.append((m[0], m[1]))
	asymp += m[0]
asymp /= N
for i in l:
	if (2*asymp - i[0], i[1]) not in l:
		flag = False
		break
if (flag):
	print('Yes')
else:
	print('No')



