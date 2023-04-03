# counting using normal method
def countDigits(n):
    i = 0
    while n > 0:
        i += 1
        n //= 10
    return i


# counting number of digits using recursion

def count_using_recursion(n):
    if n == 0:
        return 0
    return 1 + count_using_recursion(n // 10)


print(count_using_recursion(490000))
