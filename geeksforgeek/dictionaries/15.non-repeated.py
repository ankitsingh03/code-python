str = "geeksforgeeks"
k = 3

a = {i: str.count(i) for i in str}
print(sorted(a.items(), key=lambda item: item[1])[k-1][0])
print([i for i in a if a[i] == 1][k-1])
