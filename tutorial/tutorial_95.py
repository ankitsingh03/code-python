def square(number):
    square = []
    for i in number:
        square.append(i*i)
    return square
# number = [1,2,3,4]
number = list(range(1,11))
print(square(number))
