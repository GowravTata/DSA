def find_first_occurence(arr, n):
    for i in range(0, len(arr) - 1):
        if arr[i] == n:
            return i
    return -1


def first_occurence_search(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        s = l[mid]
        if x > s:
            low = mid + 1
        elif x < s:
            high = mid - 1
        else:
            if mid == 0 or l[mid] != l[mid - 1]:
                return mid
            else:
                high = mid - 1
    return -1


print(first_occurence_search(l=[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 6, 6, 6, 6], x=3))
