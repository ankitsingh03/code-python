# def even(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i
def even (n):
    return (i for i in range(2,n+1,2))


for i in even(10):
    print(i)






