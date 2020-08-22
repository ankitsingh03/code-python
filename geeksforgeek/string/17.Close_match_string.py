patterns = ['ape', 'apple', 'peach', 'puppy']
word = 'appel'

for i in patterns:
    if set(i) == set(word):
        print(i)
