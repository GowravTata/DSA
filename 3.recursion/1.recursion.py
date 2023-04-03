def fun1(integer):
    if integer <= 0:
        return  # 'Done'
    print('Gowrav')


# print(fun1(5))


def factorial(n):
    if n in (0, 1):
        return 1
    else:
        print(n)
        return n * factorial(n - 1)


# print(factorial(5))


def find_sum(n):
    if n <= 1:
        return 1
    return n + find_sum(n - 1)


# print(find_sum(10))

# fibonacci series


def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(15))

def all_numbers(n):
    if n == 0:
        return
    print(n)
    all_numbers(n - 1)
    print(n)


# print(all_numbers(6))


def fun(n):
    if n < 0:
        return
    if n == 0:
        return
    fun(n - 1)
    print(n)
    fun(n - 1)


print(fun(-4))
