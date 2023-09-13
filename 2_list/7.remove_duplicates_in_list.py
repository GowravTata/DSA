new_lists = [10, 20, 20, 30, 30, 30, 30]


# most simple solution
def remove_duplicates(input_list):
    new_list = []
    for i in input_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


# print(remove_duplicates(new_lists))


def remove_duplicates_in_list(input_list):
    input_list.sort()
    i = 0
    while i < len(input_list):
        for j in input_list[i + 1:]:
            if j == input_list[i]:
                input_list.remove(j)
        i += 1
    return input_list


# optimised solution
def remove_duplicates_best(input_list):
    j = len(input_list) - 1
    while j > 0:
        if input_list[j] == input_list[j - 1]:
            input_list.remove(input_list[j - 1])
        j -= 1
    return input_list


print(remove_duplicates_best(input_list=new_lists))

