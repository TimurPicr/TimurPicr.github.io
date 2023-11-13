m = 6
s = "AB0TAEL0ANANAB0EVO0SANAN"
n = int(len(s)/m)
array = []
for i in range(n):
	array.append(s[int(i*len(s)/n):int(i*len(s)/n)+int(len(s)/n)])
for i in range(len(array)):
	array[i] = array[i][::-1]
print(''.join(array))
