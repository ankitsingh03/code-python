winning_number = 63
number = int(input("enter your number : "))
if number == winning_number:
    print("you win !!!")
else:
    if number < winning_number:
        print("to low")
    # if number>winning_number:
    #     print("to high")
    else:
        print("to high")
