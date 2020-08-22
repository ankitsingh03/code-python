a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
start = int(input("enter starting position: "))
for i in range(start-1, len(a)):
    b.append(a[i])
for i in range(0, start-1):
    b.append(a[i])
print(b)
