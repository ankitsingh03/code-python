# def swap(l, pos1, pos2):
#     first = a[pos1-1]
#     second = a[pos2-1]
#     second_pop = a.pop(pos2-1)
#     first_pop = a.pop(pos1-1)
#     a.insert(pos1-1,second)
#     a.insert(pos2-1,first)
#     return a


a = [23, 65, 19, 90]
pos1 = int(input("enter first position: "))
pos2 = int(input("enter second position: "))
# print(f"sweep value is :{swap(a, pos1, pos2)}")
c = a[pos2-1]
a[pos2-1] = a[pos1-1]
a[pos1-1] = c
print(a)
# get = a[pos1-1], a[pos2-1]
# a[pos2-1], a[pos1-1] = get
# print(a)
