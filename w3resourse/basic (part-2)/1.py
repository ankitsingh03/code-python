"""check weather its unique not not unique"""

# method 1
lst = [1, 2, 3, 4, 5, 1]
unique = []
a = "unique"
for i in lst:
    if i not in unique:
        unique.append(i)
    else:
        a = "not unique"
        break
print(a)

# method 2
if lst == list(set(lst)):
    print('unique')
else:
    print("not unique")
