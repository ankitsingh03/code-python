# Input : 14, 625, 498.002
# Output : 14.625.498, 002

a = "14, 625, 498.002"
b = str(a).replace('.', ',').replace(',', '.', 2).replace(' ', '').replace(',', ', ').replace("5, 4", "5.4")
# print(type(a))
print(b)
# print(b[:11]+" "+b[11:])
# print(b.index(","))
