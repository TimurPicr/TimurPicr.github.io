with open('file1.txt', 'r') as f:
	s = f.readlines()
counter = 0
l = []
for i in s:
	l += i.split(' ')
for i in l:
	if ('.' in i or '!' in i or '?' in i):
		counter += 1
print(counter)
