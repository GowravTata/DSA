"""
It is a quadratic time worse case

Insertion Sort it in-place , which in turn means it doesn't use any extra space
Insertion sort is always good for small arrays

Best case is when the array is already sorted, worst case is it is inversely sorted
"""


def insertion_sort_own(input_array):
    """
    Here in the input array , the comparison is started from the first element and then ,
    the element is compared with each element and is swapped with the element where it has to be
    placed
    :param input_array:
    :return:
    """
    for i in range(1, len(input_array)):
        for j in range(0, i):
            if input_array[i] < input_array[j]:
                input_array[i], input_array[j] = input_array[j], input_array[i]
                j += 1
        i += 1
    return input_array


"""
In the below example, the comparison starts from 5, it is compared with 20 and the element is 
inserted in its index, 

For i=4 
10 is compared with 60 and replaced with 60 in the 10th position,
10 is compared with 40 and replaced with 40 in the 60th position,
10 is compared with 20 and replaced with 20 in the 40th position,
Now the while loop fails , and the x which is 10 , is replaced in i+1 position which is 1
at last x is 
"""
sample_array = [20, 5, 40, 60, 10, 30]


def insertion_sort(l):
    for i in range(1, len(l)):
        x = l[i]
        j = i - 1
        while j >= 0 and x < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = x
    return l


print(insertion_sort(sample_array))
