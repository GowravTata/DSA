# User function Template for python3

# You only need to insert the given element at
# the end, i.e., at index sizeOfArray - 1. You may
# assume that the array already has sizeOfArray - 1
# elements.
def insertAtEnd(arr, size_of_array, element):
    arr.append(element)
    return arr


arr = [1, 2, 3, 4, 5]
size_of_array = len(arr)
element = 6

print(insertAtEnd(arr=arr, size_of_array=size_of_array, element=element))

# Unfortunately I was not able to utilise size of array :)