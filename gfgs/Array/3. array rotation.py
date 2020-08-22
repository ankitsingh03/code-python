def rotate(lst, l):
    for i in range(l):
        lst.append(lst.pop(0))
    return lst


lst = [1, 2, 3, 4, 5]
print(rotate(lst, 2))

