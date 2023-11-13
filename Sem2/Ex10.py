array = [ 'а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я' ]
with open('file2.txt', 'r') as f:
	l = f.readlines()
s = l[0]
ans = ''
for i in s:
	if i in array:
		ans += 'с' + i
	else:
		ans += i
print(ans)
