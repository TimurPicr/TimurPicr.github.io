import matplotlib.pyplot as plt
import csv

op = []
cl = []

with open("BTC_data.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    
    for row in file_reader:
    	if (row[1] != 'open'):
    		op.append(int(row[1]))
    		cl.append(int(row[4]))
    		
length = len(op)
    		
def sma(close, n):
	arr = []
	for i in range(n):
		arr.append(sum(close[:n])/n)
	for i in range(n, len(close)):
		arr.append(sum(close[i-n:i])/n)
	return arr
	
	
def ema(close, n):
	arr = []
	a = 2/ (n + 1)
	for i in range(len(close)):
		if(len(arr) == 0):
			arr.append(close[i])
		else:
			arr.append(a*close[i] + arr[-1]*(1-a))
	return arr

def give_money(f, s, op, cl):	
	fast = sma(cl, f)
	slow = ema(cl, s)

	cash = 1
	status = True
	for i in range(len(op)):
		if (fast[i] <= slow[i] and fast[i-1] > slow[i-1]):
			cash = cash * cl[i]
			status = True
		elif (fast[i] >= slow[i] and fast[i-1] < slow[i-1]):
			cash = cash / op[i]	
			status = False
	if (status):
		return cash
	else:
		return cash * cl[-1]
	
	
plt.plot([i for i in range(length)], cl)
plt.plot([i for i in range(length)], ema(cl, 100), label="EMA 60")
plt.plot([i for i in range(length)], ema(cl, 20), label="EMA 20")

maxi = 0
f = 0
s = 0
for i in range(1, 50):
	for j in range(50, 100):
		a = give_money(i, j, op, cl)
		if (a > maxi):
			maxi = a
			f = i
			s = j
			
print(give_money(20, 50, op, cl))
print(maxi, f, s)
plt.legend(fontsize=14)
plt.show()

