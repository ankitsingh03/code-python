string = "100111"
p = set(string)
if p == {"0","1"} or p == {'0'} or p == {'1'}:
    print(True)
else:
    print(False)