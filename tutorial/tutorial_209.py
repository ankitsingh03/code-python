def divide(x, y):
    return x / y


while True:
    try:
        a = int(input("enter number a : "))
        b = int(input("enter number b : "))
        if b == 0:
            print("divide by zero not possible")
            continue
    except ValueError:
        print("don't enter dictonary")
    except:
        print("unexpected error")
    else:
        print(f"answer is {divide(a, b)}")
        break
