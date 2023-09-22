# #ex1
# N = int(input())
# def fibbonachi(N):
#     if(N==1):
#         return 1
#     elif (N == 2):
#         return 2
#     else:
#         return (fibbonachi(N-1)) + fibbonachi(N-2)
# print(fibbonachi(N-1))

#ex2
# N = int(input())
# def func(N, c=2):
#     if(N==1):
#         return 0
#     elif(N%c == 0):
#         print(c)
#         func(int(N/c), c)
#     else:
#         func(N, c+1)
# func(N)

# #ex3--------------------------------------
# a = 6
# b = 4
# def euc(a, b, c=1, x=0, y=1):
#     if(a%c == 0 and b%c == 0 and (x + y) < ):
#         print("d = ", c)
#     else:
#         return()

# #ex4
# def func(size, symb, var=0):
#     if (var != int(size/2)+1):
#         print(symb*var)
#         print(func(size, symb, var+1))
#         return symb*var
#     else:
#         return symb*var
# func(7, 'c')

# #ex5----------------------------------------------
# I = 6
# J = 8
# table = [0 * I][0 * J]
# counter = 1
# for i in range(0, I):
#     for j in range(0, J):

# #ex6
# X = [1, 2, 3, 4, 5]
# Y = [2, 4.5, 7.8, 11, 16]
# def MMS(X, Y):
#     sumx = sum(X)
#     sumx2 = 0
#     for i in range(0, len(X)):
#         sumx2 += X[i] * X[i]
#     sumy = sum(Y)
#     sumxy = 0
#     for i in range(0, len(X)):
#         sumxy += X[i] * Y[i]
#     a = (sumxy*len(X)-sumx*sumy)/(len(X)*sumx2-sumx**2)
#     b = (sumx2*sumy-sumxy*sumx)/(len(X)*sumx2-sumx**2)
#     print(a)
#     print(b)
#
# MMS(X, Y)

