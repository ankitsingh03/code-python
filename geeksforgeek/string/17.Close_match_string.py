patterns = ['ape', 'apple', 'peach', 'puppy','paple']
word = 'appel'

for i in patterns:
    if sorted(i) == sorted(word):
        print(i)
