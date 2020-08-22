# def odd_even(num):
#     even =num[::2]
#     odd = num[1::2]
#     total=[]
#     total.append(even)
#     total.append(odd)
#     return total
# num=[0,1,2,3,4,5,6,7]
# print(odd_even(num))

def odd_even(num):
    even=[]
    odd=[]
    for i in range(len(num)):
        if num[i]%2==0:
            even.append(num[i])
        else:
            odd.append(num[i])
    total=[even,odd]
    return total
num=[0,1,2,3,4,5,6,7,8,9,10]
print(odd_even(num))