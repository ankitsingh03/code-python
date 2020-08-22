def data_type(num):
    count = 0
    for i in num:
        if type(i) == list:
            count += 1
    return count


n = [1, 2, [3, 4], 5, [6, 7]]
print(f"your count of list are :{data_type(n)}")
