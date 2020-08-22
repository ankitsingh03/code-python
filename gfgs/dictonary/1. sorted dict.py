key_value = {}
key_value[2] = '64'
key_value[1] = '69'
key_value[4] = '23'
key_value[5] = '65'
key_value[6] = '34'
key_value[3] = '76'
# sorted by key
for i in sorted(key_value):
    print(i, end=" ")
print()

for i in sorted(key_value.items()):
    print(i, end=" ")
print()
print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))
