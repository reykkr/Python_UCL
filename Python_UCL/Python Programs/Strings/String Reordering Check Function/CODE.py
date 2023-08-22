word1 =input("Enter the first word: ")
word2 = input("Enter the second word: ")
def reorder(s1,s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for i in s1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in s2:
        if i in count:
            count[i] -= 1
        else:
            return False
    for i in count:
        if count[i] != 0:
            return False
    return True
print(reorder(word1,word2))