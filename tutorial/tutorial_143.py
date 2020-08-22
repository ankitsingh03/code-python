def cube(n,*args):
    if args:
        return [i**n for i in args]
    else:
        return "hey you didn't pass any thing"

num = []
print(cube(3))