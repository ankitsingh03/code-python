n = 5
lst = []
for i in range(n):
    lst2 = []
    for j in range(i+1):
        if j == 0 or j == i:
            lst2.append(1)
        else:
            lst2.append(lst[i-1][j-1] + lst[i-1][j])
    lst.append(lst2)
for i in lst:
    for j in i:
        print(j, end="  ")
    print()

