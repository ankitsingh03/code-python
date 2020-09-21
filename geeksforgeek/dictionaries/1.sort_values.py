# example 1
key_value = {2: 64, 1: 69, 4: 23, 5: 65, 6: 34, 3: 76}
for i in sorted(key_value.keys()):
    print(i, end=" ")
print()

# example 2
key_value = {2: 64, 1: 69, 4: 23, 5: 65, 6: 34, 3: 76}
for i in sorted(key_value.items()):
    print((i), end=" ")
print()

# example 3
key_value = {2: 64, 1: 69, 4: 23, 5: 65, 6: 34, 3: 76}
a = sorted([i[::-1] for i in key_value.items()])
print([i[::-1] for i in a])

#example 4
key_value = {2: 64, 1: 69, 4: 23, 5: 65, 6: 34, 3: 76}
print(sorted(key_value.items(), key=lambda item: item[1]))
