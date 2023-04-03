input_list_1 = [1, 5, 0, 7, 8, 9]


def check_sorted(input_list):
    for index in range(0, len(input_list) - 1):
        if not input_list[index] <= input_list[index + 1]:
            return False
        index += 1
        return True


# print(check_sorted(input_list=input_list))


def check_sorted_while(input_list):
    index = 1
    while index < len(input_list):
        if input_list[index] < input_list[index - 1]:
            return False
        index += 1
    return True


print(check_sorted_while(input_list=[1, 1, 2 ,2 ,3]))


# using sorted method

def check_list_is_sorted(input_list):
    sorted_list = sorted(input_list)
    return input_list == sorted_list

# print(check_list_is_sorted(input_list=input_list_1))
