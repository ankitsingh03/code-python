def monotonic(lst):
    for i in range(1,len(lst)):

        if lst[i-1] >= lst[i]:
            yield True
        else:
            yield False


lst = "6 5 4 4".split()
print(all(list(monotonic(lst))))
