n = input("enter number: ")
sum = 0
for i in n:
    sum += int(i)**len(n)
if sum  == int(n):
    print("yes")
    print(f"{n} is an armstrong number")
    print(sum)
else:
    print("no")
    print(f"{n} is not an armstrong number")
    print(sum)