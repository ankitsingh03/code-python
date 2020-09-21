a = 'geeksforgeeks'
string = ''
for i in a:
    if i not in string:
        string += i
print(string)

print("".join(sorted(set(a))))
