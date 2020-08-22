# DSA-Assgn-1

def merge_list(list1, list2) :
    n = len(list1)
    # list2.reverse()
    data = ""
    for i in range(n):
        if list2[i] == None:
            data = data + list1[i]+" "
        else:
            data = data + list1[i] + list2[n-i-1]+" "
    return data


# Provide different values for the variables and test your program
list1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']
print(merge_list(list1, list2))
# print(merged_data)
