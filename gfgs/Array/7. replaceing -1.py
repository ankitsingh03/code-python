def func(lst, m):
    for i, j in enumerate(lst):
        # print(i)
        if j == -1:
            lst[i] = (lst[i-1] +1) % m
    return lst


lst = [5, -1, -1, 1, 2, 3]

print(func(lst, 11))