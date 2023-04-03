def updateArray(arr, n, idx, element):
    if idx < n:
        arr[idx] = element
    return arr


print(updateArray(arr=[1, 2, 3, 4], n=4, idx=2, element=23))
