array = [1, 2, 3, 2, 3, 3]
counter = 0
var = 0
for i in array:
	if(array.count(i) > counter):
		counter = array.count(i)
		var = i
print(var)
