name = ['abc','pqr','xyz']
names = [i[::-1] for i in name]
print(names)

name1 = []
for i in name:
    name1.append(i[::-1])
print(name1)