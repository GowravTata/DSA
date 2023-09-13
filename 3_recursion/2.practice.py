def fun(N):
    if N <= 1:
        return 0
    return 1 + fun(N / 2)


print(fun(N=34))

# this number gives the binary representation of a number

def fun_two(number):
    if int(number) == 0:
        return
    fun_two(number / 2)
    print(int(number % 2))


print(fun_two(number=13))
