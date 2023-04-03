# Input:
# N = 3
# arr[] = {1,2,3}
# Possible Answer: 2
# Generated Output: 1
# Explanation: index 2 is 3.
# It is the peak element as it is
# greater than its neighbour 2.
# If 2 is returned then the generated output will be 1 else 0

ls = [6, 1, 15, 19, 9, 13, 12, 6, 7, 2, 10, 4, 1, 14, 11, 14, 14, 13]


def peak_finder(l, n):
    index = 0
    i = 0
    while i < n - 1:
        if l[i] <= l[i + 1]:
            index += 1
            i += 1
        else:
            index = i
            break
    return index


def peakElement(arr, n):
    l = 0
    r = n - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return l


l_s = [6, 1, 15, 19, 9, 13, 12, 6, 7, 2, 10, 4, 1, 14, 11, 14, 14, 13]

print(peak_finder(l=l_s, n=len(l_s)))
