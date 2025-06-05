def lomutopartition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def qSort(arr, l, h):
    if l < h:
        p = lomutopartition(arr, l, h)
        qSort(arr, l, p - 1)
        qSort(arr, p + 1, h)

    return arr


arr = [7,1,4,9,23,12,2]
l = 0
h = len(arr) - 1
print(qSort(arr, l, h))


