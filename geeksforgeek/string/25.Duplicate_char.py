# Input : geeksforgeeeks
# Output : e g k s
string = "geeksforgeeeks"
temp =""
s = set()
for i in string:
    if i not in temp:
        temp += i
    else:
        s.add(i)
for j in sorted(s):
    print(j, end=" ")


