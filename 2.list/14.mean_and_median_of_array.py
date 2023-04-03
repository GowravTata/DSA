def median(A, N):
    A.sort()
    N = N - 1
    if N % 2 == 0:
        return int(A[int((N + 1) / 2)])
    return int((A[int(N / 2)] + A[int((N / 2) + 1)]) / 2)


def mean(A, N):
    return int(sum(A) / N)


a = [1, 2, 3, 4, 5]

n = len(a)

print(mean(A=a, N=n))
print(median(A=a, N=n))
