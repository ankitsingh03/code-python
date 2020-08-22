def Isprime(n):
    if n <= 1:
        return "Invalid"
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(Isprime(17))
