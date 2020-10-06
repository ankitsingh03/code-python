"""
3. Write a Python Code that takes input as the values of x, y, a, b to solve the following equation:
[ {x + (1/y) }^a * {x – (1/y)}^b] / [ {y + (1/x) }^a * {y – (1/x)}^b]
"""


def cal(x, y, a, b):
    if x <= 1 and y <= 1:
        return " x and y should not be one"

    eq1 = (x+(1/y))**a
    eq2 = (x-(1/y))**b
    eq3 = (y+(1/x))**a
    eq4 = (y-(1/x))**b

    return (eq1 * eq2) / (eq3 * eq4)


x, y, a, b = map(float, input("enter x, y, a, b with comma separated: ").split(","))
print(cal(x, y, a, b))
