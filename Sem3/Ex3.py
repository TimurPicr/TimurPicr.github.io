a = 5
b = 3
      
def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n
d = gcd(a, b)
def euc(a, b, d, x, y):
	if (a*x + b*y == d):
		return (x, y)
	elif (x > 0):
		return euc(a, b, d, -x, int((1/b)*(d + a*x)))	
	else:
		return euc(a, b, d, -x + 1, int((1/b)*(d + a*(x-1))))
ans = euc(a, b, d, 0, 0)
print(min(ans), max(ans), d)
  
