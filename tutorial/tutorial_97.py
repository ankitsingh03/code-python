def rev(number):
    reverse = []
    for i in range(len(number)):
        reverse.append(number.pop())
    return reverse
a =  [4,5,6,7,8]
print(rev(a))