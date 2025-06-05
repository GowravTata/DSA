"""
We take all the elements, we run the array once and take the element with
minimum index and replace the element, then after that loop is incremented so that
numbers are increased from left to right, after each loop element that is to be present
in its place is positioned
"""
def selection_sort(input_list):
    n = len(input_list)
    for i in range(n - 1):
        i += 1
        min_index = i
        for j in range(i + 1, n):
            if input_list[j] < input_list[min_index]:
                min_index = j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
        i += 1
    return input_list


input_list_1 = [-17, 4, 9, 2, 11]
print(selection_sort(input_list_1))
