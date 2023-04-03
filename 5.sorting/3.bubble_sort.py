# time complexity of this algorithm is theta of n square in the worst case, and linear time in the best case
#  bubble sort is the only algorithm that does not use auxiliary space or random data

def bubble_sort(l):
    n = len(l)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):  # this condition is necessary to eliminate the elements which are sorted
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
        if not swapped:
            return l
    return l


ls = [2, 7, 6, 5]
print(bubble_sort(ls))
