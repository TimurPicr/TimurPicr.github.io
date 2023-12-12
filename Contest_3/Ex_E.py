def my_sort(array):
    if (len(array) == 2):
        return [min(array), max(array)]
    elif (len(array) == 1):
            return array
    elif (len(array) == 0):
        return []
    else:
        var = array[0]
        left = []
        center = []
        right = []
        for i in array:
            if (i < var):
                left.append(i)
            elif (i == var):
                center.append(i)
            else:
                right.append(i)
        return my_sort(left) + center + my_sort(right)
abuba = list(map(int, input().split()))
l = abuba[1] 
array = list(map(int, input().split()))
array = my_sort(array)[::-1]
vals = []


for i in range(len(array)):
	a = 0
	k = 0
	for j in range(len(array)):
		if (array[j] >= array[i]):
			a += 1
		else:
			if (k < l):
				if (array[j] + 1 == array[i]):
					a += 1
					k += 1
				else:
					break
			else:
				break
	vals.append(a)

for i in range(len(array)):
	vals[i] = min((array[i], vals[i]))
print(max(vals))
	
