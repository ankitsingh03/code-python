# method 1
def sum_square(n):
    return sum(i**2 for i in range(1,n+1))


print(sum_square(5))

# method 2
print(sum(i**2 for i in range(int(input("enter number: "))+1)))
