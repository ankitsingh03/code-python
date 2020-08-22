def fibinacci():
    a = 0
    b = 1
    yield a
    yield b
    for i in range(50):
        c = a + b
        a = b
        b = c
        yield c


num = int(input("enter number to check: "))
for i in fibinacci():
    if i == num:
        print("YES")
        break
else:
    print("NO")
