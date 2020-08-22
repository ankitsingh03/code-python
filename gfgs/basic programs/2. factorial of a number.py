# method 1
def factorial(n):
    total = 1
    for i in range(n,0,-1):
        total *= i
    print(total)


factorial(4)

# method 2
def fact(x):
    return 1 if x==1 else x * fact(x-1)


print(fact(4))
