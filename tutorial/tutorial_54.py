num = input("enter number to sum each digit: ")
i = 0
total = 0
while i < len(num):
    total = total + int(num[i])
    i += 1
print(total)
