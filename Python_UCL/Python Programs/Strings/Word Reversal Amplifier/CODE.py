word = input("Enter a word")
nb = int(input("Enter an integer"))
def switch(s,i):
    reverse = ""
    for j in s:
        reverse = j + reverse
    if i > 0:
        word = i * reverse
        return word
    else:
        i = i * -1
        word = i * reverse
        return word
print(switch(word,nb))