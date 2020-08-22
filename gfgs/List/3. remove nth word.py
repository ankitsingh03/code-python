def word(lst, wrd, n):
    inc = 0
    for i in range(n):
        index = lst.index(wrd, inc)
        inc = index + 1
    lst.pop(index)
    return lst



# lst = ["geeks", "for", "geeks"]
# wrd = "geeks"
# n = 2
# print(word(lst, wrd, n))

lst = ["can", "you",  "can", "a", "can","?"]
wrd = "can"
n = 3
print(word(lst, wrd, n))
