import random
a = random.randint(1,100)
i=1
n=int(input("gussa number 1 to 100 : "))
while True:
    if n==a:
        print(f"you win and you guss {i} time")
        break
    elif n < a:
        print("too low")
    else:
        print("too high")

    n = int(input("guss again : "))
    i+=1
