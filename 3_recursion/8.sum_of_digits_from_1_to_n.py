# sum of all digits from 1 to n

def sum_all_numbers(n):
    a = 0
    for i in range(1, n + 1):
        a += i
    return a


print(sum_all_numbers(5))


def sum_all(n):
    if n in (0, 1):
        return n
    return n + sum_all(n - 1)


print(sum_all(5))
