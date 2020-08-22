def duplicate(x):
    temp = []
    dup = []
    for i in x:
        if i not in temp:
            temp.append(i)
        else:
            dup.append(i)
    print(dup)
    print(list(set(dup)))


a = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
duplicate(a)
