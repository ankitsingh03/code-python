# method 1
def armstrong(n):
    return sum(int(i)**len(n) for i in n) == int(153)


print(armstrong('153'))


# method 2
def armstrong1(n):
    string = 0
    for i in n:
        string += int(i)**len(n)
    return string == int(n)


print(armstrong1("153"))
