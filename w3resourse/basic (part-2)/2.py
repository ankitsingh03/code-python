"""Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly
once """

vowel = {'a', 'e', 'i', 'o', 'u'}
string = "aeo ui"
ans = True
for i in vowel:
    if string.count(i) == 1:
        continue
    else:
        ans = False
print(ans)
