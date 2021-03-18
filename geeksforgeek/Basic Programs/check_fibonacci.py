def fibonacci(n):
    # 0, 1, 1, 2, 3,5
    a = 0
    b = 1
    if n == a:
        return True
    
    while not (b > n):
        c = a + b
        a = b
        b = c
        if b == n:
            return True
    return False


num = int(input("enter number you want to check"))
print(fibonacci(num))
