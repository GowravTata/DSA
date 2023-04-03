import math

def digitsInFactorial(N):
    if N<0:
        return 0
    if N<=1:
        return 1
    dig = 0
    for i in range(2,N+1):
        dig+=math.log10(i)
    return math.floor(dig)+1    

print(digitsInFactorial(120))