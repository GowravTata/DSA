def maximumElement(arr, n):
    maxer = arr[0]
    for i in range(n):
        maxer = max(maxer, arr[i])
    return maxer

    # code here


def minimumElement(arr, n):
    mini = arr[0]
    for i in range(n):
        mini = min(mini, arr[i])
    return mini


array = [1, 2, 3, 4, 5]

size = len(array)

print(maximumElement(arr=array, n=size))
print(minimumElement(arr=array, n=size))
