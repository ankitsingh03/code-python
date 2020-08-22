# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)
#
# negative = [-i for i in range(1,11)]
# print(negative)

name = ['ankit','rohit','harshit']
names = []
for i in name:
    names.append(i[0])
print(names)

names1 = [i[0] for i in name]
print(names1)