string = "geeks for geek"
sub_string = "geek"
if string.find(sub_string) == -1:
    print("Not present")
else:
    print("present")

# second method
if sub_string in string:
    print("present")
else:
    print("not present")
