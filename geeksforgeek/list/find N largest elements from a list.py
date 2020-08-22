a = [81, 52, 45, 10, 3, 2, 96]
n = 3
b = []
for i in a:
    if a[n] <= i:
        b.append(i)
print(b)
# print([i for i in a if a[n-1] <= i])
