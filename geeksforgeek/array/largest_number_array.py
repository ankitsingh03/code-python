a = [15, 4, 11, 10, 5, 12]
# print(max(a))
maximum = a[0]
for i in a:
    if i > maximum:
        maximum = i
print(maximum)
