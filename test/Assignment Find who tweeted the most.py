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

"""
Test Cases:

Sample 1:
Input:
1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4

Output:
sachin 3

Sample 2:
Input:
1
6
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
kohli tweet_id_5
kohli tweet_id_6

Output:
kohli 2
sachin 2
sehwag 2

Sample 3:
Input:
2
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
5
dhoni tweet_id_10
dhoni tweet_id_11
kohli tweet_id_12
dhoni tweet_id_13
dhoni tweet_id_14

Output:
sachin 2
sehwag 2
dhoni 4
"""