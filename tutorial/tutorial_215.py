# with open('file1.txt','a') as f:
#     f.write("\nhello")
f = open('file.txt')
print(f.read())
for i in f:
    print(i)