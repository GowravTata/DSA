ls = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62
    , 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90
    , 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]


def findFloor(A, N, X):
    low = 0
    high = N - 1
    second_least = -1
    if X > A[high]:
        return high
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == X:
            return mid
        if A[mid] < X:
            low = mid + 1
            second_least = mid
        elif A[mid] > X:
            high = mid - 1
    return second_least


print(findFloor(A=ls, N=79, X=212))
