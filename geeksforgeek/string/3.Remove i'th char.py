a = "GeeksForGeek"
pos = int(input("enter position to remove value: "))
new_str = ""
for i in range(len(a)):
    if i != pos-1:
        new_str += a[i]
print(new_str)


# comprehension
print("".join([a[i] for i in range(len(a)) if i != pos-1]))

# slicing
print(a[:pos-1]+a[pos:])