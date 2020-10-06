"""
1. Create a Python Function to perform a calculation based on the following mathematical function

i=n
 ∑ 1/(x^i)
i=1

Do not use the Math library to perform this task. Perform this task using two different methods. One of
the methods should be using recursion.
"""


# method 1
def solve(n, x):
    if x <= 0:
        return "x should not be zero"
    add = 0
    for i in range(1, n+1):
        add += 1 / (x ** i)
    return add


# method 2 (Recursion)
def recursion(n, x, i=1):
    if x <= 0:
        return "x should not be zero"
    if i == n+1:
        return 0

    return (1/(x**i)) + recursion(n, x, i+1)


n = 7
x = 2
print(recursion(n, x))
print(solve(n, x))
