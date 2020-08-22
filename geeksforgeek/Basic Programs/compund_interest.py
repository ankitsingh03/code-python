p = float(input("enter principle : "))
r = float(input("enter rate : "))
t = float(input("enter time :"))
compound = p*(1+r/100)**t
print(f"your compound interest is : {compound}")
