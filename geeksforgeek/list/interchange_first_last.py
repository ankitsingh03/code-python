a = [12, 35, 9, 56, 24]
first = a.pop(0)
last = a.pop()
a.insert(0,last)
a.append(first)
print(a)