def smallerThan(arr, n, x):
    arr.sort()
    count = 0
    for i in arr:
        if i < x:
            count += 1
        if i >= x:
            break
    return count


def smallerThanX(arr, n, x):
    arr.sort()
    count = 0
    for i in arr:
        if i < x:
            count += 1
    return count


def smallerThanXd(arr, n, x):
    arr.sort()
    i = 0
    while i < n and arr[i] < x:
        i += 1
    return i


# most efficient solution, this method doesn't use sort oto find the numbers that are less than the given number
# this uses all the variables that are predefined in the question
def smallerThanXf(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] < x:
            count += 1
    return count


arr = [1, 1, 1, 1, 2, 3, 4, 5]
N = len(arr)
X = 1

print(smallerThanXf(arr=[4, 5, 3, 1, 2], n=5, x=3))
