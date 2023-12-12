N = int(input())
def fibbonachi(N):
    if(N==1):
        return 1
    elif (N == 2):
        return 2
            else:
        return (fibbonachi(N-1)) + fibbonachi(N-2)
print(fibbonachi(N-1))
