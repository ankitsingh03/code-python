TestCase = int(input())
Total_List = []

for i in range(TestCase):
    Tweets_List = []
    length = int(input())add

    # push the values of input
    for j in range(length):
        Tweets_List.append(input().split()[0])

    Name_count = {i: Tweets_List.count(i) for i in Tweets_List}

    # find maximum count of name
    Maximum_Count = max(Name_count.values())

    # push name with maximum count
    Name = {i: Maximum_Count for i in Name_count if Name_count[i] == Maximum_Count}
    Total_List.append(Name)

# iterate the total_list which contain dict of name and count of name
for i in Total_List:
    for m, n in sorted(i.items()):
        print(m, n)
