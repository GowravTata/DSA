import time


def SieveOfEratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, num + 1):
        if prime[p]:
            print(p)


num = 730


# SieveOfEratosthenes(num)


def sieve(n):
    if n <= 1:
        return
    is_prime = [True] * (n + 1)
    i = 2
    while i * i <= n:
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[i] = False
        i += 1
    for i in range(2, n + 1):
        if is_prime[i]:
            print(i, end=" ")


sieve(17)
