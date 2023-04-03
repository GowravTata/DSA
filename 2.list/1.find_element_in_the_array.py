# check if the element is present in the array, if not return -1

# given arr is the array , n is the size of the array, idx is the index number

def getByIndex(arr, n, idx):
    return arr[idx] if idx <= n else -1


arr = list(range(1, 5))

print(getByIndex(arr=arr, n=len(arr), idx=3))
