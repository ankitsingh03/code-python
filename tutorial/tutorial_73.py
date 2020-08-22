# def big(a,b):
#     if a>b:
#         print(f"this is bigger {a}")
#     else:
#         print(f"this is bigger {b}")
#
# a = int(input("enter first number : "))
# b = int(input("enter second number : "))
# print(big(a,b))

def big(a,b):
    if a>b:
        return a
    return b
a = int(input("enter first number : "))
b = int(input("enter second number : "))
print("this is bigger "+str(big(a,b)))