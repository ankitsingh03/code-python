str = "GEEGEEKSKS"
sub_str = "GEEK"
if sub_str in str:
    print("Yes")
else:
    print("No")

if str.find(sub_str) == -1:
    print("no")
else:
    print("yes")