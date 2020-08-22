# a = [1,2,3]
# print(sum(a))

def _sum(n):
    sum = 0
    for i in n:
        sum += i
    return sum


print(_sum([1,2,3]))