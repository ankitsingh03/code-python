def SI(p, r, t):
    return (p*r*t)/100


p, r, t = tuple(map(float, input("enter p r t: ").split()))
print(SI(p, r, t))
