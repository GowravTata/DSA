new_list = [1, 2, 3, 4, 5]


def rotate_list(input_list, number):
    return input_list[number:] + input_list[:number]


def rotateArr(A, D, N):
    return A[D:] + A[:D]


print(rotateArr(A=new_list, D=2, N=5))


def rotate_given_list(input_list):
    length = len(input_list) - 1
    for i in range(length):
        input_list[i], input_list[i - 1] = input_list[i - 1], input_list[i]
        i += 1
    return input_list

#
# print(new_list)
# print(rotate_list(input_list=new_list, number=1))
# print(rotate_given_list(input_list=new_list))
