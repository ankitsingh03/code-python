def intersection(x, y, z):
    uncommon = []
    for i in x:
        if (i in y) and (i in z):
            uncommon.append(i)
            x.remove(i)
            y.remove(i)
            z.remove(i)
    print(uncommon)


ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

if len(ar1) > len(ar2) and len(ar1) > len(ar3):
    intersection(ar1, ar2, ar3)
elif len(ar2) > len(ar1) and len(ar2) > len(ar3):
    intersection(ar2, ar1, ar3)
else:
    intersection(ar3, ar1, ar2)


# another method

def Counter(x):
    return {i: x.count(i) for i in x}


# not good for those if the single value is repeat in same list and nor repeat in other two

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
ar1 = Counter(ar1)
ar2 = Counter(ar2)
ar3 = Counter(ar3)
resultDict = dict(ar1.items() & ar2.items() & ar3.items())
print([i for i in resultDict.keys()])
