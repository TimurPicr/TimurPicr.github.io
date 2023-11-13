n = 5
array = [3, 1, 2, 5, 4]

for i in array:
	l = 0
	h = 0
	for j in array:
		if (j <= i):
			l += 1
		else:
			h += 1
	l = l - 1 #Удаляю рассматриваемый элемент
	if (h == l):
		print(i)
		break
