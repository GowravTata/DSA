def print_all(n):
    if n > 0:
        print_all(n - 1)
        print(n)


print_all(13)


# printing numbers reverse from n to 1

def print_all_reverse(n):
    if n > 0:
        print(n)
        print_all_reverse(n - 1)

# print_all_reverse(13)
