new_inp = [10, 30, 1215, 78, 32, 156, 1215]
new_inp_2 = [1215, 17, 30, 12156, 78, 32, 156, 12115]


def find_max_element(input_list):
    new = input_list[0]
    for i in range(1, len(input_list)):
        new = max(new, input_list[i])
    return new


# Inefficient Solution
def find_second_largest_element_1(input_list):
    largest = find_max_element(input_list=input_list)
    second_largest = None
    for x in input_list:
        if x != largest:
            if second_largest is None:
                second_largest = x
            else:
                second_largest = max(second_largest, x)
    return second_largest


# print(find_second_largest_element_1(input_list=new_inp))


def find_second_largest_element_2(input_list):
    if not input_list:
        return None
    else:
        first_largest = input_list[0]
        second_largest = 0

        for element in input_list:
            if element > first_largest:
                second_largest = first_largest
                first_largest = element
            elif element != first_largest and element > second_largest:
                second_largest = element
        return second_largest


third_input_list = [10, 20, 30, 40, 50]
new_inps = [10, 30, 1215, 78, 32, 156, 1234, 1215]
print(find_second_largest_element_2(input_list=third_input_list))


# most efficient method

def find_second_largest_element_3(input_list):
    largest = input_list[0]
    second_largest = None
    for x in input_list[1:]:
        if x > largest:
            second_largest = largest
            largest = x
        elif x != largest:
            if second_largest is None or second_largest < x:
                second_largest = x
    return second_largest


third_input_list = [10, 20, 30, 40, 50]

# print(find_second_largest_element_2(input_list=third_input_list))
