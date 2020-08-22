# method 1
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
print(lst.index(x))

# method 2
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
for i in range(len(lst)):
    if lst[i] == x:
        print(i)
        break

# method 3
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
for i,j in enumerate(lst):
    if j == x:
        print(i)
        break
