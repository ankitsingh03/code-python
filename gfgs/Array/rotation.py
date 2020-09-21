from array import array

t = int(input())
for i in range(t):
    n, r = tuple(map(int, input().split()))
    l = list(map(int, input().split()))
    # print(*(l[n-r:]+l[:n-r]))
    x = r % n             #mostimp concept
    print(*(l[n-x:]+l[:n-x]))


def left_rotation(arr, d, n):
    for i in range(d):
        temp = arr[0]
        for j in range(n-1):
            arr[j] = arr[j + 1]
        arr[n-1] = temp


lst = array('i', [1, 2, 3, 4, 5])
d, n = 2, len(lst)
left_rotation(lst, d, n)
print(lst)


