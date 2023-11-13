s = 'AOA'


mirror = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
half_mirror_1 = ['E', 'J', 'S', 'Z']
half_mirror_2 = ['3', 'L', '2', '5']

is_pal = True
is_mirror = True

s_v = s[::-1]
if (s != s_v):
	is_pal = False	
for i in range(len(s)):
	if (s[i] in mirror):
		if (s[i] != s_v[i]):
			is_mirror = False
			break
	elif (s[i] in half_mirror_1 and s_v[i] in half_mirror_2):
		if(half_mirror_1.index(s[i]) != half_mirror_2.index(s_v[i])):
			is_mirror = False
	elif (s[i] in half_mirror_2 and s_v[i] in half_mirror_1):
		if(half_mirror_2.index(s[i]) != half_mirror_1.index(s_v[i])):
			is_mirror = False
	else:
		is_mirror = False
if (is_pal):
	if (is_mirror):
		print("Mirrored palindrome")
	else:
		print("Not mirrored palindrome")
else:
	if (is_mirror):
		print("Mirrored not palindrome")
	else:
		print("Not mirrored not palindrome")
	
