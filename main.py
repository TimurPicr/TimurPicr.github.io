# #ex1
# a = 5
# b = 4
# print(a + b, a - b, a * b, sep='\n', end='\n')
#
#
# #ex2
# n = 123456
# print(n%10)
#
# #ex3
# A = list(map(int, input().split()))
# count = 0
# for i in range(0, len(A), 1):
#     count += A[i]
# print(count)

# #ex4
# f = open('input.txt', 'r')
# array = list(map(int, f.readline().split()))
# chara = f.readline()
# f.close()
# f = open('output.txt', 'w')
# if (chara == '+'):
#     counter = 0
#     for i in array:
#         counter += i
#     f.write(str(counter))
# elif (chara == '-'):
#     counter = 0
#     for i in array:
#         counter -= i
#     f.write(str(counter))
# elif (chara == '*'):
#     counter = 1
#     for i in array:
#         counter *= i
#     f.write(str(counter))

# #ex5
# N = "1a34z5"
# b = 12
# c = 5
# digits = '0123456789abcdefghijklmnopqrstuvwxyz'
# digit = 0
# j = 1
# for i in N:
#     digit += digits.find(i) * b**(len(N)-j)
#     j += 1
# #digit = 14432256
# digitAns = ""
# i = 1
# while digit != 0:
#     digitAns += digits[digit%(c)]
#     i += 1
#     digit = digit//(c)
# print(str(digitAns)[::-1])

# #ex6
# def toDigit(N, b):
#     digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#     digit = 0
#     j = 1
#     for i in N:
#         digit += digits.find(i) * b**(len(N)-j)
#         j += 1
#     return digit
#
# def toNewDigit(N, b):
#     digitAns = ""
#     i = 1
#     digit = int(N)
#     while digit != 0:
#         digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#         digitAns += digits[digit % (b)]
#         i += 1
#         digit = digit // (b)
#     return int((digitAns)[::-1])
#
# f = open('input.txt', 'r')
# array = f.readline().split(' ')
# c = f.readline()
# b = int(f.readline())
# array[len(array) - 1] = array[len(array)-1][0:len(array)-2]
# newArray = []
# for i in array:
#     newArray.append(str(toDigit(i, int(b))))
# count = 0
# c = c[0:len(c)-1]
# if(c == '+'):
#     for i in newArray:
#         count += int(i)
# elif(c == '*'):
#     count = 1
#     for i in newArray:
#         count *= int(i)
# elif(c == '-'):
#     for i in newArray:
#         count -= int(i)
# print(toNewDigit(count, b))