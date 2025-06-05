"""
My approach to merge sorted arrays
"""


def mergeSortedArrays(a, b):
    new_list = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            new_list.append(a[i])
            i += 1
        else:
            new_list.append(b[j])
            j += 1
    while i < len(a):
        new_list.append(a[i])
        i += 1
    while j < len(b):
        new_list.append(b[j])
        j += 1
    return new_list


# a = [10, 15]
# b = [5, 6, 6, 30, 40]
# print(mergeSortedArrays(a,b))


def mergeSubarraysOwnFunction(a, mid, high):
    new_list = []
    i = 0
    j = mid + 1
    while i <= mid and j <= high:
        if a[i] < a[j]:
            new_list.append(a[i])
            i += 1
        else:
            new_list.append(a[j])
            j += 1
    while j < len(a) and j >= len(new_list):
        new_list.append(a[j])
        j += 1
    while i < len(a) and i >= len(new_list):
        new_list.append(a[i])
        i += 1
    return new_list


# a = [10, 15, 20, 40, 8, 11, 55]
low = 0
high = 6
mid = 3

"""
My approach to merge subarrays which are already sorted
"""


# a = [10, 15, 20, 40, 8, 11, 55]
# low = 0
# high = 6
# mid = 3


def merge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]
    i = 0
    j = 0
    index = low
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[index] = left[i]
            i += 1
            index += 1
        else:
            a[index] = right[j]
            j += 1
            index += 1
    while i < len(left):
        a[index] = left[i]
        i += 1
        index += 1
    while j < len(right):
        a[index] = right[j]
        j += 1
        index += 1
    return a


print('Merge Sort')


# print(merge(a, low, mid, high))


def mergeSort(arr, l, r):
    if r > l:
        m = (r + l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr


de = [9, 1, 4, 6, 3, 12]
print('Recursive Function')
print(mergeSort(de, low, high))

a = [10, 15, 20, 40, 8, 11, 55]

print(merge(a, low, mid, high))
