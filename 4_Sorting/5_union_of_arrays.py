def mergeSortedArrays(a, b):
    new_list = []
    duplicate = False
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            if a[i] not in new_list:
                new_list.append(a[i])
                i += 1
            else:
                i += 1
        else:
            if b[j] not in new_list:
                new_list.append(b[j])
                j += 1
            else:
                j += 1
    return new_list


a = [2, 20, 20, 40]
b = [1, 10, 20]
print_list = []
i = 0
j = 0
while i < len(a) and j < len(b):
    if i > 0 and a[i] == a[i - 1]:
        i += 1
    elif j > 0 and b[j] == b[j - 1]:
        j += 1
    elif a[i] < b[j]:
        print(a[i], end=" ")
        i += 1
    elif a[i] > b[j]:
        print(b[j], end=" ")
        j += 1
    else:
        print(a[i], end=" ")
        i += 1
        j += 1
while i < len(a):
    if i > 0 and a[i] != a[i - 1]:
        print(a[i], end=" ")
    i += 1
while j < len(b):
    if j > 0 and b[j] != b[j - 1]:
        print(b[j], end=" ")
    j += 1

