def func(name):
    return [i[-1::-1].title() for i in name]
name=['ankit','mohit']
print(func(name))