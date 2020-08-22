# method 1
def Isprime(a, b):
    for i in range(a, b+1):
        if i == 1:
            pass
        elif i == 2:
            print(2)
        elif i > 2:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


Isprime(1, 10)


# method 2
def Isprime1(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(tuple(filter(Isprime1, (i for i in range(1,)))))
