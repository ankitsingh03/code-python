start = int(input("enter starting point: "))
end = int(input("enter ending point: "))
# print([i for i in range(start,end+1) if i % 2 == 0])
for i in filter(lambda a: a % 2 == 0, range(start, end+1)):
    print(f"{i},", end=" ")
