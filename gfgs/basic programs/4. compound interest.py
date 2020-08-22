def CI(P, R, T):
    return P*(1 + R/100)**T


P, R, T = tuple(map(float, input("enter P R T: ").split()))
print(CI(P, R, T))
