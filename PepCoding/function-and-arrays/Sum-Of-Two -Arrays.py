count1 = int(input())
lst1 = []
for i in range(count1):
    lst1.append(int(input()))
count2 = int(input())
lst2 = []
for i in range(count2):
    lst2.append(int(input()))
if count1 > count2:
    diff = abs(count2-count1)
    for i in range(diff):
        print(lst1[i])
    i += 1
    for j in range(count2):
        print(lst1[i] + lst2[j])
        i += 1
else:
    diff = abs(count2 - count1)
    for i in range(diff) :
        print(lst2[i])
    i += 1
    for j in range(count1) :
        print(lst2[i] + lst1[j])
        i += 1

'''5
  3 1 0 7 5
6
1 1 1 1 1 1
'''