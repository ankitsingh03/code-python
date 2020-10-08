n = 5
array = [3, 4, 1, 2, 0]
i = 0
inv = [i for i in range(n)]
for i in range(n):
    temp_1 = array[i]
    inv[temp_1] = i
print(inv)
