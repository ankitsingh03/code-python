def rev_list(word1):
    word2 = []
    for i in word1:
        word2.append(i[::-1])
    return word2
word = ["abc","tuv","xyz"]
print(rev_list(word))