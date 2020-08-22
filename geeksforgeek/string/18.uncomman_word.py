def uncomman(a,b):
    new = []
    if len(a) >= len(b):
        return [i for i in a if i not in b]
    else:
        return [i for i in b if i not in a ]

a = "Geeks for Geeks car".split()
b = "Learning from Geeks for Geeks".split()
print(uncomman(a, b))
