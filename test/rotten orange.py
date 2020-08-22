arr = [[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
count = 0

for m in range(len(arr)):
    for n in range(len(arr[0])):
        a = arr[m][n]
        if a == 2:

            if m > 0:
                if arr[m - 1][n] == 1:
                    arr[m + 1][n] = 2

            if m != len(arr)-1:
                if arr[m + 1][n] == 1:
                    arr[m + 1][n] = 2

            if n != len(arr[0])-1:
                if arr[m][n + 1] == 1:
                    arr[m][n + 1] = 2

            if n > 0:
                if arr[m][n - 1] == 1:
                    arr[m][n - 1] = 2

    count += 1

print(count - 1)
