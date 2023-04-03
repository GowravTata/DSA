def sumOfDigits(n):
    i = 0
    while n > 0:
        i += n % 10
        n //= 10
    return i


number = 400


# print(sumOfDigits(number))


# sum of digits using recursion

def recursion_digit_sum(n):
    if n == 0:
        return 0
    return recursion_digit_sum(n // 10) + n % 10


print(recursion_digit_sum(4900))
