votes = ["john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"]

a = {i: votes.count(i) for i in votes}
max_values = max(a.values())
lst = [i for i in a.keys() if a[i] == max_values]
print(sorted(lst)[0])