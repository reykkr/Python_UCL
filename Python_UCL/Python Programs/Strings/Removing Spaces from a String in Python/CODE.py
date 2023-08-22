word = input("Enter a string")
def no_space(s):
    count = ""
    for i in s:
        if i not in " ":
            count += i
    return count
print(no_space(word))

# Another way

# word = input("Enter a string:")
# def No_Space(word):
#     s = " "
#     for c in word:
#         if c != " ":
#             s = s + c
#     return s
# print(No_Space(word))