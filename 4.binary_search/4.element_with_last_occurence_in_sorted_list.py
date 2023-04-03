def find_last_occurence(arr, n):
    for i in range(-(len(arr) - 1), 0):
        if arr[i] < n:
            return -1
        if arr[i] == n:
            return i
    return -1


def last_element_occurrence(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] < x:
            low = mid + 1
        elif l[mid] > x:
            high = mid - 1
        else:
            if mid == len(l) - 1 or l[mid] != l[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1


print(last_element_occurrence([1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 8, 9, 10], 8))
