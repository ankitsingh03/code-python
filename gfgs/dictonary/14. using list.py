arr = ['cat', 'dog', 'tac', 'god', 'act']
lst = ["".join(sorted(i)) for i in arr]
print(lst)
a = {i: lst.count(i) for i in lst}
print(a)
rev_A = sorted(a, key=lambda item: a[item], reverse=True)
print(rev_A)
nlst = []
for i in rev_A:
    for j in arr:
        if sorted(i) == sorted(j):
            nlst.append((j))
print(nlst)
