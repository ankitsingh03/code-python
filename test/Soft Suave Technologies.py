def solve(arr):
    m, n = 0, 0
    lst = [arr[m][n]]

    while True:
        if m < 2:
            a = arr[m + 1][n]
        else:
            for k in range(n + 1, 3):
                lst.append(arr[m][k])
            break

        if n < 2:
            b = arr[m][n + 1]
        else:
            for k in range(m + 1, 3):
                lst.append(arr[k][n])
            break

        if a > b:
            lst.append(a)
            m = m + 1
        else:
            lst.append(b)
            n = n + 1

    print(lst)
    print(abs(sum(lst)) + 1)


solve([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
solve([[-3, 4, -4], [-1, -5, 3], [-1, 2, -4]])
solve([[-9, -6, 5], [2, 5, -3], [3, -4, -5]])
