char = "geeksforgeeeks"

a = {i: char.count(i) for i in char}
print(a)
for key, value in a.items():
    if value > 1:
        print(key, end=" ")
