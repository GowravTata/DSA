
n=5

def factorial(n):
    val=1
    while n>0:
        val*=n
        n-=1
    return val

print(factorial(5))


def factoria_nl(N):
    if N ==0:
        return 1
    else:
        return N*factoria_nl(N-1)

print(factoria_nl(6))