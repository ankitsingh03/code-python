def reminder(lst, n):
    total = 1
    for i in lst:
        total *= i
    return total % n


lst = [100, 10, 5, 25, 35, 14]
n = 11
print(reminder(lst, n))