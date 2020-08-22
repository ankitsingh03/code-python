# list1 = [2, 7, 5, 64, 14]
a  = input("enter number with comma: ").split(",")
print([int(i) for i in a if int(i) % 2 == 0])
# print(list(filter(lambda a:int(a) % 2 == 0, a)))
