def Isprime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return "wrong input"


print(Isprime(24))
