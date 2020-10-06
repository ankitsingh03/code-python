string = input()
balance = 0

for i in string:
    if balance < 0:
        break

    if i == '(':
        balance += 1
    else:
        balance -= 1

if balance == 0:
    print('balance')
else:
    print("unbalance")
