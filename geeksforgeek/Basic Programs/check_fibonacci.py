def fibonacci(n):
    # 0, 1, 1, 2, 3,5
    a = 0
    b = 1
    for j in range(n):
        c = a + b
        a = b
        b = c
        yield b


num = int(input("enter number you want to check"))
for i in fibonacci(1000):
    if num == i:
        print(f"this {i} is fibonacci")
        break
