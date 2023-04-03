def find_largest(input_list):
    for x in input_list:
        for y in input_list:
            if y > x:
                break
        else:
            return x
    return None


inp = [10, 30, 5, 78, 32]


# print(find_largest(input_list=inp))


def find_largest_element(input_list):
    max_element = input_list[0]
    for element in input_list:
        if element > max_element:
            max_element = element
    return max_element


new_inp = [10, 30, 5, 156, 78, 1212, 32, 156]


# print(find_largest_element(input_list=new_inp))

def find_max_element(input_list):
    new = input_list[0]
    for i in range(1, len(input_list)):
        new = max(new, input_list[i])
    return new


# print(find_max_element(input_list=new_inp))
