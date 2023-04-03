def reverseArray(arr, n):
    right_element = n - 1
    left_element = 0
    while left_element < right_element:
        arr[left_element], arr[right_element] = arr[right_element], arr[left_element]
        left_element += 1
        right_element -= 1
    return arr


array = list(range(1, 41))

size = len(array)
print(reverseArray(arr=array, n=size))
