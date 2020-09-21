def uncomman(a,b):
    yield (i for i in a if i not in b)
    yield (i for i in b if i not in a)

a = "Geeks for Geeks car".split()
b = "Learning from Geeks for Geeks".split()
for i in uncomman(a, b):
    print(*list(i), end=" ")
