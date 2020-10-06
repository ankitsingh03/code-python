n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

max = lst[0]
for i in range(n):
    if max < lst[i]:
        max = lst[i]

for i in range(max, 0, -1):
    for j in range(n):
        if i <= lst[j]:
            print('*', end="\t")
        else:
            print("", end="\t")
    print()
