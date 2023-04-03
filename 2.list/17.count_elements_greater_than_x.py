def greaterThanX(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] > x:
            count += 1
    return count


print(greaterThanX(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n=10, x=5))
