# Input: list - ["geeks", "for", "geeks"]
#        word = geeks, N = 2
# Output: list - ["geeks", "for"]
list1 = ["can", "you",  "can", "a", "can", "?"]
word = 'can'
n = 2
count = 0
if word in list1:
    for i in range(n):
        list1.remove(word)
    print(list1)

else:
    print("you enter word in not present in list")


