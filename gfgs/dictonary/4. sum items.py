d = {'a': 100, 'b':200, 'c':300}

# method 2
sum1 = 0
for i in d.values():
    sum1 += i
print(sum1)

# method 2
print(sum(d.values()))
