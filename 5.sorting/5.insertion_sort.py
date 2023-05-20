"""
    In place: doesn't use any use auxiliary space
    stable: retaining the position of equal elements
    most popular and most efficient algorithm for small arrays'
    python uses tim sort : uses a combination of merge sort and insertion sort

"""

sample_array = [20, 5, 30, 40, 60, 10, 30, 30]


def insertion_sort_own(l):
    n = len(l)
    for i in range(1, n):
        first_element = i
        for j in range(i):
            if l[j] > l[first_element]:
                first_element = i
                l[j], l[first_element] = l[first_element], l[j]
    return l


def insertion_sort(l):
    for i in range(1, len(l)):
        x = l[i]
        j = i - 1
        while j > 0 and x < l[j]:
            l[j + 1] = l[i]
            j = j - 1
        l[j + 1] = x
    return l


print(insertion_sort(l=sample_array))

