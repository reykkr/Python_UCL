word = input("Enter a word")
reverse = ""
for i in word:
    reverse = i + reverse

if word == reverse:
    print("is a palindrome")
else:
    print("is not a palindrome")

# Another way

# word = input(("Enter a word"))
# def isPalindrome(s):
#         low = 0
#         high = len(s) - 1
#         while low < high:
#             if s[low] != s[high]:
#                 return False
#             low += 1
#             high -= 1
#         return True
# print(isPalindrome(word))

# Another way

# word = input(("Enter a word"))
# def ispalindrome(z):
#     r = ""
#     for i in range(len(s)-1, -1, -1):
#         r = r + s[i]
#     if r == z:
#         return True
#     else:
#         return False
# print(ispalindrome(word))