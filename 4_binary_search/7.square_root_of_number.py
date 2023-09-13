def find_square_root(x):
    j = 1
    for i in range(2, x):
        if x % i == 0 and x >= i:
            j *= i
            x //= i
    return j


print(find_square_root(7))
