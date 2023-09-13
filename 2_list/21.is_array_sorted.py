def isSorted(arr, n):
    index = 1
    first_list = True
    second_list = True
    while index < n:
        if not arr[index] <= arr[index - 1]:
            first_list = False
            break
        index += 1
    while index < n:
        if not arr[index] >= arr[index - 1]:
            second_list = False
            break
        index += 1
    return first_list or second_list


newsd = [3, 2, 2, 2, 1, 1]

print(isSorted(arr=newsd, n=5))