num = input("enter array with comma separated: ").split(',')
div = int(input("enter number to divide: "))
multiply = 1
for i in num:
    multiply *= int(i)
print(multiply)
print(multiply % div)
