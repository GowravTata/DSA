"""
     selection sort has less memory writes compared to any other algorithm, but not the best,
     cycle optimal is the best algorithm
     it always has a time complexity of theta square n for all the scenarios
     It is the basic idea for heapsort
     not stable, order of equal elements may change
"""

# my solution
"""
   in the below approach swapping is done for every loop that is, the first index element is directly swapped
   by comparing the elements with all the remaining elements
"""


def selection_sort_own(l):
    n = len(l)
    for i in range(n - 1):
        for j in range(i, n):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


# Actual solution
def selection_sort(l):
    n = len(l)
    for i in range(n - 1):
        mid_elem = i
        for j in range(i + 1, n):
            if l[j] < l[mid_elem]:
                mid_elem = j
        l[mid_elem], l[i] = l[i], l[mid_elem]
    return l


array = [10, 5, 8, 20, 2, 18, 10, 9, 10]

some = list(range(1, 10))
print(selection_sort_own(l=array))

