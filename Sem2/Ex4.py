array = [1, 2, 3, 4, 5]



def f(s):
	if (len(s) < 2):
		return str(s[0])
	else:
		return str(s[1]) + ' ' + str(s[0]) + ' ' + f(s[2:])
		
print(f(array))

