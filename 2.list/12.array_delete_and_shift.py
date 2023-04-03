def deleteFromArray(arr, n, idx):
    if idx <= n - 1:
        del arr[idx]
        arr.append(0)
    return arr


print(deleteFromArray([1, 2, 3, 4], 4, 2))
