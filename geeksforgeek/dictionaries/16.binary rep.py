a, b = 4, 8
print(bin(a))
print(bin(b))
num1 = sorted(bin(a)[2:])
print(num1)
num2 = sorted(bin(b)[2:])
print(num2)
if num1 == num2:
    print("yes")
else:
    print(("no"))