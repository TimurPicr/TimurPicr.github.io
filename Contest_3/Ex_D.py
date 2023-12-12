def f(array, r):
	if (len(array) == 0):
		return 0
	elif (len(array) == 1):
		return 1
	else:
		a = array[0] + 2*r
		non_array = []
		for i in array:
			if (i > array[0] + 2*r):
				non_array.append(i)
		return 1 + f(non_array, r)


	
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
N = abuba[0]
r = abuba[1]
array = list(map(int, input().split()))
array = my_sort(array)
print(f(array, r))
