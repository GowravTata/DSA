# reversing the 2.list using library methods

def reverse_list(input_list):
    return list(reversed(input_list))


def reverse_list_2(input_list):
    input_list.reverse()
    return input_list


def reverse_list_three(input_list):
    return input_list[::-1]


def reverse_input_list(input_list):
    new_list = []
    i = len(input_list) - 1
    while i >= 0:
        new_list.append(input_list[i])
        i -= 1
    return new_list


def reverse_list_by_swapping(input_list):
    right_element = len(input_list) - 1
    left_element = 0
    while left_element < right_element:
        input_list[left_element], input_list[right_element] = input_list[right_element], input_list[left_element]
        left_element += 1
        right_element -= 1
    return input_list


def reverse_list_by_swappingas(arr, n):
    right_element = n -1
    left_element = 0
    while left_element < right_element:
        arr[left_element], arr[right_element] = arr[right_element], arr[left_element]
        left_element += 1
        right_element -= 1
    return arr


print(reverse_list_by_swappingas(arr=[1, 1, 2, 2, 3], n=5))
