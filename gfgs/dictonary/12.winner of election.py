a = ["john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"]
d = {i: a.count(i) for i in a}
m = max(d.values())
lst = [i for i in d if d[i]==m]
print(lst)
print(min(lst, key= lambda i:len(i)))
