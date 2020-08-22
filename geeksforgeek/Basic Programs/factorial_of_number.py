#4----->4*3*2*1
number = int(input('enter number: '))
multiply = 1
for i in range(1, number+1):
    multiply *= i
print(f'your factorial is : {multiply}')
