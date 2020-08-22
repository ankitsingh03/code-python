# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe"
#          Right Rotation : "ksGeeksforGee"

s = "GeeksforGeeks"
d = 3
print(f"left slice  {s[d:]+s[:d]}")
print(f"right slice  {s[-d:]+s[:len(s)-d]}")