input_array = [10, 20, 30, 40, 50, 60]


def binary_search(l, x, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    if l[mid] == x:
        return mid
    elif l[mid] > x:
        return binary_search(l, x, low, mid - 1)
    else:
        return binary_search(l, x, mid + 1, high)


def bsearch_two(l, x):
    return binary_search(l, x, 0, len(l) - 1)


print(bsearch_two(input_array, 60))
