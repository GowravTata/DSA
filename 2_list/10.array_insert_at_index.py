def insertAtIndex(arr, size_of_array, index, element):
    arr.insert(index, element) if index < size_of_array else arr
    return arr


array = [1, 2, 3, 4, 5]
size = 5
idx = 2
element = 27

print(insertAtIndex(arr=array, size_of_array=size, index=idx, element=element))
