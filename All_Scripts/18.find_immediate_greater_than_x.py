def immediateGreater(arr, n, x):
    arr.sort()
    elem = -1
    for i in range(n):
        if arr[i] > x:
            elem = arr[i]
            break
    return elem


print(immediateGreater(arr=[1, 2, 3, 4, 5, 6, 7, 8], n=8, x=5))
