def check_num_palin(n):
    reverse_num = 0
    temp = n
    while n > 0:
        last_digit = n % 10
        reverse_num = reverse_num * 10 + last_digit
        n = n // 10
    return reverse_num == temp


# print(check_num_palin(100))

n = 1332


# checking if a number is palindrome using recursion by typecasting it as string

def isPalin(N):
    n = str(N)
    if len(n) == 1:
        return 1
    if n[0] == n[- 1]:
        return isPalin(n[1:- 1])
    return 0


print(isPalin(100))
