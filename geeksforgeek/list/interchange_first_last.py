# method 1
a = [12, 35, 9, 56, 24]
first = a.pop(0)
last = a.pop()
a.insert(0,last)
a.append(first)
print(a)

# method 2
a = [12, 35, 9, 56, 24]
temp = a[0]
a[0] = a[len(a)-1]
a[len(a)-1] = temp

print(a)
