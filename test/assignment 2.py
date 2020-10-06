"""
2. Write a Python function to find the next number in the series:
   ==> 2, 3, 10, 15, 26, 35, 50, 63, ?
"""


def func(n):
    if n < 1:
        print("enter positive number")
        return
    a = 2
    b = 3
    c = 10
    if n == 1:
        print(a)
    elif n == 2:
        return print(a, b)
    elif n == 3:
        return print(a, b, c)
    else:
        print(a, b, c, end=" ")
        for i in range(0, n-3):
            x = b - a + 4
            a, b, c = b, c, c+x
            print(c, end=" ")


n = 0
func(n)
