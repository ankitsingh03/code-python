t = int(input())
for _ in range(t):
    string = list(map(int, input()))
    count = 0
    for i in string:
        if i == 1:
            count += 1
    if count == 1:
        print(0)
        break
    elif count == 2:
        print(1)
        break
    else:
        print((count - 2) * 3)
        break
