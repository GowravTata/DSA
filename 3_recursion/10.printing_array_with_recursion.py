arra = [1, 2, 3, 4]

size = len(arra)


# submitted solution
def array_recursion(arr, n):
    i = 0
    while i < n:
        print(arr[i], end=" ")
        i += 1


def print_array_recursion(arr, n):
    if n == 0:
        return
    print_array_recursion(arr, n - 1)
    print(arr[n - 1], end=" ")


print(print_array_recursion(arra, size))
