test_case = int(input())
total_list = []
for i in range(test_case):
    total_list.append(input().split())
    # total_list.append()
sorted_list = sorted(total_list, key=lambda i: (i[1], i[2], int(i[3][0:2]), int(i[3][3:5],int(i[3][6:]))))
for i in sorted_list:
    print(i[0])


# ,int(i[3][0:2]),int(i[3][3:5],int(i[3][6:])
'''
S1 Rajdeep 10 25/10/2020
S2 Rajdeep 10 25/10/2020
S3 Rajdeep 11 25/11/2020
S4 Rajdeep 11 25/10/2020
S5 Alok 12 25/10/2020
S6 Alok 12 25/10/2020
S7 Alok 11 25/10/2020
S8 Alok 11 25/11/2020
'''
