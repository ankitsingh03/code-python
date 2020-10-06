# a = [-2, 3, 1, -5]
a = [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5]

for x in range(0,999):
    sum = x
    for j in a:
        sum += j
        if sum < 1:
            break

    if sum >= 1:
        print(x)
        break
