a = [2, 10, 20, 20, 20, 40]
b = [1, 10, 10, 10, 20]

dups = []
i = 0
j = 0
while i < len(a) and j < len(b):
    if i > 0 and a[i - 1] == a[i]:
        i += 1
        continue
    elif a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    elif a[i] in dups:
        i += 1
    elif b[j] in dups:
        i += 1
    else:
        print(a[i])
        i += 1
        j += 1


