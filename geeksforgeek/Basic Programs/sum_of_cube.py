def sum_power(n, p):
    return sum((i**p for i in range(1, n+1)))


# sum = 0
# for i in sum_power(5, 2):
#     sum += i
# print(sum)
print(sum_power(5, 2))
