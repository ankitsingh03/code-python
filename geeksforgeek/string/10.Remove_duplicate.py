a = 'geeksforgeeks'
temp = ""
string = ''
for i in a:
    if i not in temp:
        temp += i
        string+= i
print(string)
print("".join(set(a)))
