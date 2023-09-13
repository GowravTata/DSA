# naive approach
def count_element(l, x):
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


def last_element_occurrence(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] < x:
            low = mid + 1
        elif l[mid] > x:
            high = mid - 1
        else:
            if mid == len(l) - 1 or l[mid] != l[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1


def find_count(l, x):
    first_count = first_occurence_search(l, x)
    if first_count == -1:
        return 0
    return last_element_occurrence(l, x) - first_count + 1


print(find_count(l=[1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6], x=8))
