lst = list("35004")
print(lst.index('7'))
while '0' in lst:
	lst.remove('0')
	lst.append('0')
print(lst)
