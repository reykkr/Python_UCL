word = input("Enter a word: ")
def letter(a):
    j = ''
    for i in a:
        if i == j:
            return True
        j = i
    return False
print(letter(word))