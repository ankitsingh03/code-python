"""
0
1   1
2   3   5
8   13  21  34
55  89  144 233 377
"""

n = 5
a, b = 0, 1
for i in range(1, n+1):
    for j in range(i):
        print(a, end=" ")
        # temp = a
        # a = b
        # b = temp + b
        b, a = a+b, b
    print()
