"""
Merge sort works on the principle of divide and conquer, that is it divides the work that is
present and then works on the other things
It is a stable algorithm
not an in place algorithm
It takes big of N auxiliary space
It is well suited for externally sorting
Generally Merge Sort is outperformed by Quick Sort

Merge Sort is still used in many libraries

Time complexity is theta (m+1)
"""

"""
Merge and join two sorted list
"""
a = [1, 10, 20]
b = [6, 30, 60]


def merge_two_list(a, b):
    for i in b:
        a.append(i)
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a


a_list = [10, 15, 20]
b_list = [5, 6, 6, 30]


def merge_third_method(a, b):
    c = []
    a_len = len(a)
    b_len = len(b)
    start = 0
    for i in range(a_len):
        for j in range(b_len):
            if a[i] > b[j]:
                j = start
                c.append(b[j])
                j += 1
                start += 1
            else:
                c.append(a[i])
                i += 1
            start = j
    return c


def merge_list_original_from_gfg(a, b):
    """
    Here two list are taken
    a = [1, 10, 20]
    b = [6, 30, 60]

    First element from the list a is compared with the elements present in the list b,
    at that time i=0,j=0

    In the first iteration, a[i] (1), b[j] (6), as a[i] is larger, to a new list
    the value of a[i] is appended and the i value is incremented by 1,
    Now 10 is compared with 6, and it is seen that 6 is smaller than 10, as j value in list b is
    appended to the new list, value of j is incremented by 1
    """
    res = []
    m = len(a)
    n = len(b)
    i, j = 0, 0
    while i < m and j < n:
        first = a[i]
        second = b[j]
        if first < second:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < m:
        res.append(a[i])
        i += 1
    while j < n:
        res.append(b[j])
        j += 1
    return res


# print(merge_list_original(a, b))

# a = [10, 15, 20, 11, 13]
a = [5, 8, 12, 14, 7]
low = 0
high = 4
mid = 3


def merge_two_sorted_list_own_implementation(a, low, mid, high):
    new_list = []
    if a[low] < a[mid] and a[low + 1] > a[high]:
        new_list.append(a[low])
        for i in range(mid + 1, high + 1):
            new_list.append(a[i])
        for i in range(low + 1, mid + 1):
            new_list.append(a[i])
    return new_list


# print(merge_two_sorted_list(a, low, mid, high))

def merge(a, low, mid, high):
    """

    :param a: list that is to be taken
    :param low: lower index of the list
    :param mid: middle index of the list
    :param high: highest index of the list
    :return:
    a= [10, 15, 20, 40, 8, 11, 55]
    low=0
    middle=3
    high=6
    In this method , two list are taken
    left list containing the elements from low to middle, [10, 15, 20, 40]
    right list containing the elements from middle to right, [8, 11, 55]
    here the comparison starts from first element in left list to the first element in the
    right list

    one more variable k is taken, which stores the low index, this can be used to insert the
    element in its position

    in the first iteration 10 is compared with 8 and 10 is replaced with 8 in a
    so the result will be [8, 15, 20, 40, 8, 11, 55], j , k are incremented by 1

    in the second iteration i=0,j=1, 11 is compared with 10 and 15 is replaced with 10 in a
    so the result will be [8, 10, 20, 40, 8, 11, 55]

    like wise it will happen for all the iterations
    """
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]
    i, j = 0, 0
    k = low
    while i < len(left) and j < len(right):
        left_one = left[i]
        right_one = right[j]
        if left_one <= right_one:
            a[k] = left[i]
            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        a[k] = left[i]
        k += 1
        i += 1
    while i < len(right):
        a[k] = right[j]
        k += 1
        j += 1
    return a


def mergesort(arr, l, r):
    """

    :param arr:
    :param l:
    :param r:
    :return:
    """
    if r > l:
        m = (r + l) // 2
        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr


print(mergesort([10, 5, 30, 15, 7], 0, 4))
# print(merge([10, 15, 20, 40, 8, 11, 55], 0, 3, 6))
