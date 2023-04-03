def find_gcd_number(a, b):
    maxer = 1
    s = b % a
    while s > 1:
        if a % s == 0 and b % s == 0:
            maxer = s
            break
        s -= 1
    return maxer


# print(find_gcd_number(42, 60))


def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(b, a - b)


a = 25
b = 46
print(gcd(a, b))
