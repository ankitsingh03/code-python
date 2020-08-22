# def comman_no(num1,num2):
#     comman=[]
#     temp=[]
#     for i in num1:
#         for j in num2:
#             if i==j:
#
#                 comman.append(i)
#     return comman

def comman_no(num1,num2):
    output=[]
    for i in num1:
        if i in num2:
            output.append(i)
    return output
num1=[1,2,3,4,5]
num2=[1,3,6,5]
print(comman_no(num1,num2))
