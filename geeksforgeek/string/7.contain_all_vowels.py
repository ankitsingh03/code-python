# a = "geeks for geek"
a = "ABeeIghiObhkUl"
a = a.lower()
if ('a' in a) and ('e' in a) and ('i' in a) and ('o' in a) and ('u' in a):
    print("present")
else:
    print("not present")

#method 2
for i in set('aeiou'):
    if i not in a:
        print('not present')
        break
else:
    print('present')

