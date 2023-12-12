X = [1, 2, 3, 4, 5]
Y = [2, 4.5, 7.8, 11, 16]
def MMS(X, Y):
    sumx = sum(X)
    sumx2 = 0
    for i in range(0, len(X)):
        sumx2 += X[i] * X[i]
    sumy = sum(Y)
    sumxy = 0
    for i in range(0, len(X)):
        sumxy += X[i] * Y[i]
    a = (sumxy*len(X)-sumx*sumy)/(len(X)*sumx2-sumx**2)
    b = (sumx2*sumy-sumxy*sumx)/(len(X)*sumx2-sumx**2)
    print(a)
    print(b)
    
MMS(X, Y)
