burito = list(input())
stack = []
flag = True
for i in burito:
	if (i == '('):
		stack.append('(')
	elif (i == '['):
		stack.append('[')
	elif (i == '{'):
		stack.append('{')
	else:
		if (len(stack) != 0):
			a = stack.pop()
			if (i == ')' and a !='('):
				flag = False
				break
			elif (i == ']' and a !='['):
				flag = False
				break
			elif (i == '}' and a !='{'):
				flag = False
				break
			
		else:
			flag = False
			break
if (flag): 
	print('Yes') 
else: 
	print('No')
