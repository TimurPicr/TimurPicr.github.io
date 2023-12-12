N = int(input())
def func(N, c=2):
    if(N==1):
        return 0
    elif(N%c == 0):
        print(c)
        func(int(N/c), c)
    else:
             func(N, c+1)
func(N)
