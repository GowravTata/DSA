ls = [1]


def one_counter(l, x):
    low = 0
    high = len(l) - 1
    if l[-1] == x:
        return len(l)
    if l[0] == x and l[1] != x:
        return 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] < x:
            high = mid - 1
        else:
            if l[mid] == x and l[mid] != l[mid + 1]:
                return mid + 1
            else:
                low = mid + 1
    return 0


# User function Template for python3


def countOnes(arr, N):
    high, low = N - 1, 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == 0:
            high = mid - 1
        else:
            low = mid + 1

    return low


print(one_counter(ls, 1))
