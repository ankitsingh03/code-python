# method 1
a = [1, 4, 5, 7, 8]
print(a[::-1])

# method 2
a = [1, 4, 5, 7, 8]
a.reverse()
print(a)

# method 3
a = [1, 4, 5, 7, 8]
b = []
for i in range(len(a)):
    b.append(a.pop())
print(b)

# method 5
a = [1, 4, 5, 7, 8]
print(list(reversed(a)))
