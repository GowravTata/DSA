def majorityWins(arr, n, x, y):
    counter = {}
    if x not in arr:
        return x
    if y not in arr:
        return y
    for elem in arr:
        if elem in counter:
            counter[elem] += 1
        else:
            counter[elem] = 1
    if counter[x] == counter[y]:
        return min(x, y)
    if counter[x] > counter[y]:
        return x
    return y


# best solution
def majorityWinsbest(self, arr, n, x, y):
    if x not in arr and y not in arr: return min(x, y)
    if x in arr and y not in arr: return x
    if y in arr and x not in arr: return y
    counter = {}
    for elem in arr:
        if elem in counter:
            counter[elem] += 1
        else:
            counter[elem] = 1
    if counter[x] == counter[y]:  return min(x, y)
    if counter[x] > counter[y]:  return x
    return y


# best solution
def majority(arr, n, x, y):
    x1 = 0
    y1 = 0
    for i in range(n):
        if arr[i] == x:
            x1 += 1
        elif arr[i] == y:
            y1 += 1
    if x1 == y1: return min(x, y)
    if x1 > y1:
        return x
    return y


array = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7]
size = len(array)

print(majority(arr=array, n=size, x=1, y=2))
