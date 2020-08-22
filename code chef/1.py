def chef(d, c):
    while True:
        if d <= 0:
            return 0
        if c <= 0:
            return 1
        d = d - c
        c = c/2


t = int(input())
for i in range(t):
    d, c = list(map(int,input().split()))
    print(chef(d, c))