str = "geeksforgeeks"
k = 3
a = {i: str.count(i) for i in str}
print(a)
print(sorted(a.items(), key=lambda item:item[1]))
print((sorted(a.items(), key=lambda item:item[1]))[k-1][0])
