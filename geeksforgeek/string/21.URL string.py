# Input : dictonary = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles
# in the portal of http://www.geeksforgeeks.org/'
#
# Output : URLs :  ['https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles',
# 'http://www.geeksforgeeks.org/']

string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org/'
a1 = string.find("http")
a2 = string.find(" ", a1)
b1 = string.find("http", a2)
b2 = string.find(" ", b1)
print(a1, a2)
print(b1, b2)

print(f"URL: {string[a1:a2]}, {string[b1:b2]}")
