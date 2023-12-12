def my_sort(array):
    if (len(array) == 2):
        if (array[0][0] > array[1][0]):
            return [array[1], array[0]]
        else:
            return[array[0], array[1]]
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
            if (i[0] < var[0]):
                left.append(i)
            elif (i[0] == var[0]):
                center.append(i)
            else:
                right.append(i)
        return my_sort(left) + center + my_sort(right)

N = int(input())
array = []
for _ in range(N):
    boba = list(map(int, input().split()))
    array.append((boba[0], boba[1]))
sorted_array = my_sort(array)
print(sorted_array)
"""
counter = 1
i = 0
while (i != len(sorted_array) - 2 ):
	for j in range(i+1, len(sorted_array)):
		if (sorted_array[i][1] < sorted_array[j][0]):
			counter += 1
			i = j - 1
			break
	i += 1
	
print(counter)
print(sorted_array)"""
