a = [1, 2, 3, 4, 5]
b = list({i: i**3 for i in a}.items())
print(b)
print(dict(b))