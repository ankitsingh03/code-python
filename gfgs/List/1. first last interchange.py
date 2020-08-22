a = [12, 35, 9, 56, 24]

a.append(a.pop(0))
a.insert(0, a.pop(-2))
print(a)
