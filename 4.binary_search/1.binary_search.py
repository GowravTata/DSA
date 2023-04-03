def bsearch(l, x):
    l.sort()
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        s = l[mid]
        if s == x:
            return mid
        elif s < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


input_array = [10, 20, 30, 40, 50, 60, 70]

print(bsearch(input_array, 50))
