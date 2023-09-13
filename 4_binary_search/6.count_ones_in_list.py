def one_counter(l, x):
    count = 0
    for i in range(len(l)):
        if l[i] == x:
            count += 1
    return count


def first_occurence_search(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        s = l[mid]
        if x > s:
            low = mid + 1
        elif x < s:
            high = mid - 1
        else:
            if mid == 0 or l[mid] != l[mid - 1]:
                return mid
            else:
                high = mid - 1
    return -1


def ones_counter(l, x):
    first = first_occurence_search(l, x)
    if first == -1:
        return 0
    return len(l) - first


print(ones_counter(l=[0, 0, 0, 0], x=1))
