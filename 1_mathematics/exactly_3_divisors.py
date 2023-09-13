# {
# Driver Code Starts
# Initial Template for Python 3

# simple solution
def check_prime(number):
    prime = True
    if number == 2:
        return prime
    else:
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        return prime


def prime_num(x):
    for k in range(2, x):
        if x % k == 0:
            return False
    return True


def exactly3div(n):
    primes = list(range(2, int(n ** 0.5) + 1))
    new_primes = []
    for i in primes:
        if prime_num(i):
            new_primes.append(i)
    return len(new_primes)


# print(exactly3div(51))

# optimised solution for getting the exact 3 divisors
def exactly3Divisors(N):
    primes = list()
    for i in range(2, int(N ** 0.5) + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return len(primes)


print(exactly3Divisors(100))
