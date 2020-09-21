# Input : arr = ['cat', 'dog', 'tac', 'god', 'act']
# Output : 'cat tac act dog god'

arr = ['cat', 'dog', 'tac', 'god', 'act']
s = set()

for i in arr:
    key = "".join(sorted(i))
    s.add(key)

for j in sorted(s):
    for i in arr:
        if "".join(sorted(i)) == j:
            print(i, end=" ")
