# Input : arr = ['cat', 'dog', 'tac', 'god', 'act']
# Output : 'cat tac act dog god'

arr = ['cat', 'dog', 'tac', 'god', 'act']
for i in arr:
    key = "".join(sorted(i))
    # print(key)
dect = {}
dect['key'] = []
print(dect['key'])
dect['key'].append('dog')
print(dect)