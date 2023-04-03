def immediateSmaller(arr, n, x):
    elem = -1
    for i in range(n):
        while n > i and elem < arr[i] < x:
            elem = arr[i]
            i += 1
    return elem


print(immediateSmaller(arr=[1, 2, 3, 4, 5], n=5, x=3))
