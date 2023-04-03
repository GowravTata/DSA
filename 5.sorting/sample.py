def bubble(l):
    n = len(l)
    for i in range(n - 1):
        for j in range(n - i - 1):
            a, b = l[j], l[j + 1]
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


ls = [2, 10, 8, 7,89, 97]
# print(bubble(ls))

from functools import wraps
import time


def time_counter(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper
