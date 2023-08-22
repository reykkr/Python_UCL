word = input("Enter a word")
a = input("Enter a word")
def count(w,a):
    counter = 0
    for i in w:
      if i == a:
         counter += 1
    return counter
print(count(word,a))