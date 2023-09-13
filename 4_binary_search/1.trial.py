def bsearch(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


input_array = list(range(1, 11))

print(bsearch(input_array, 4))
