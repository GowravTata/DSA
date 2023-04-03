def rotateArr(A, D, N):
    new = A[D:] + A[:D]
    return new


a = [25, 6, 20, 55, 69, 5, 50, 63, 61, 41, 87, 80, 2, 96, 77, 70, 12, 43, 31, 8, 64, 41, 68, 18, 95, 79, 52, 74, 1, 98,
     3, 26, 3, 74, 32, 23, 79, 81, 37, 39, 21, 24, 18, 22, 71, 47, 44]
size = len(a)


def rotate_array(array, n, index):
    new = []
    for i in range(index, n):
        new.append(array[i])
    for i in range(index):
        new.append(array[i])
    return new


def rotate_arrays(A, D, N):
    new = []
    for i in range(D, N):
        new.append(A[i])
    for i in range(D):
        new.append(A[i])
    return new


def rotate_arrays_by_index(A, D, N):
    if D > N:
        for i in range(D % N, N):
            A.insert(0, A.pop())
    else:
        for i in range(D - N, 0):
            A.insert(0, A.pop())
    return A


def rotate_given_array(A, D, N):
    if D > N:
        for i in range(D % N, N):
            A.insert(0, A.pop())
        return A
    for i in range(D - N, 0):
        A.insert(0, A.pop())
    return A


new_B = list(range(1, 6))
b_size = len(new_B)
print(rotate_given_array(A=new_B, D=2, N=b_size))

# print(rotate_arrays(A=a, D=2, N=size))

# print(rotate_array(a, size, 2))
