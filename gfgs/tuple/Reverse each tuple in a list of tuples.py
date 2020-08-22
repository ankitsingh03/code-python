Input = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
# Output : [(2, 1), (5, 4, 3), (9, 8, 7, 6)]
lst = []
for i in Input:
    lst.append(tuple(reversed(i)))
print(lst)
a = (1, 2, 3)
print(a[::-1])
