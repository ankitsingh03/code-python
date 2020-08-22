def fibonacci(n):
    # 0, 1, 1, 2, 3, 5
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(b)
    else:
        print(a, b, end=" ")
        for j in range(n - 2):
            c = a + b
            a = b
            b = c
            print(b, end=" ")


fibonacci(5)
