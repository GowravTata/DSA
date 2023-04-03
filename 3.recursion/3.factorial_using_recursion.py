def factorial(n):
    i = 1
    while n > 1:
        i *= n
        n -= 1
    return i


# print(factorial(5))

def recursive_factorial(n):
    if n in (0, 1):
        return 1
    return n * recursive_factorial(n - 1)


print(factorial(5))
