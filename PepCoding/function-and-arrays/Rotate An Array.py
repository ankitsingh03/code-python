n = 5
lst = [1, 2, 3, 4, 5]
k = -102

if k >= 0:
    k = k % n
    for i in lst[-k:]+lst[:-k]:
        print(i,end=" ")
else:
    k = (-k) % n
    for i in lst[k:]+lst[:k]:
        print(i, end=" ")