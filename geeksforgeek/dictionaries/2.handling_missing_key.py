d = { 'a' : 1 , 'b' : 2 }
a = input()
if a in tuple(i for i in d.keys()):
    print(d[a])
else:
    print("key nor present")