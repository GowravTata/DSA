a = [10, 20, 30, 40]

counter = 0

n = len(a)

for i in range(n - 1):
    for j in range(i + 1, n):
        if i < j and a[i] > a[j]:
            counter += 1

print(counter)


def counterMerge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]
    i = 0
    j = 0
    index = low
    res=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[index] = left[i]
            i += 1
        else:
            a[index] = right[j]
            j += 1
            res+=(len(left)-i)
        index += 1
    while i < len(left):
        a[index] = left[i]
        i += 1
        index += 1
    while j < len(right):
        a[index] = right[j]
        j += 1
        index += 1
    return res

print(counterMerge(a=[2,5,8,11,3,6,9,13],low=0,mid=3,high=7))

def counterInv(arr, l, r):
    res=0
    if r > l:
        m = (r + l) // 2
        res+=counterInv(arr, l, m)
        res +=counterInv(arr, m + 1, r)
        res += counterMerge(arr, l, m, r)
    return res
