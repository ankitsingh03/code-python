def func(word,same):
    for pos,i in enumerate(word):
        if i==same:
            return (f"{pos}---{i}")
    return -1
word = ['ankit','abc','xyz']
same = 'xyz'
print(func(word,same))
