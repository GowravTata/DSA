def printGP(first, second, ratio):
    if second - first == 1:
        return int((second / first) ** (ratio - 1))
    return first + ((second - first) * (ratio - 1))


#

f = 87
s = 93
r = 5


def find(a, b, n):
    r = a / b
    t2 = r ** (n - 1)
    if r > 1:
        return a * (t2 / (r - 1))
    return a * ((1 - (r ** n)) / (1 - r))


# print(find(84, 87, 5))


new_list = [198, 5, 6, 7, 3, 54, 16, 25, 981]


# print(new_list)


def find_second_largest(new_list):
    max = new_list[0]
    for i in new_list:
        if i > max:
            max = i
    new = new_list[0]
    for i in new_list:
        if i > new and i < max:
            new = i
    return new


def calc_largest(arr):
    second_largest = arr[0]
    largest_val = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest_val:
            largest_val = arr[i]

    for i in range(len(arr)):
        if arr[i] > second_largest and arr[i] != largest_val:
            second_largest = arr[i]

    return second_largest


# print(calc_largest(arr=new_list))
# print(find_second_largest(new_list=new_list))

s = '2[AB]3[C]4[D]'

output = ''

for ch in s:
    if ch.isnumeric():
        x = int(ch)
    if ch.isalpha():
        output = output + x * ch
# print(output)


