string = "geeksforgeeeks"
a = {i: string.count(i) for i in string}
lst = (i for i in a.keys() if a[i] > 1)
for i in sorted(lst):
    print(i, end=" ")