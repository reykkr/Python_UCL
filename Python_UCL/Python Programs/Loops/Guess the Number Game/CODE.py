import random

nb = random.randint(0, 5)
tries = 0
sentinel = -9
n = eval(input("TYPE A NUMBER"))
while nb != n and tries < 4 and n != sentinel:
     if nb > n:
        print("the number is greater than yours")
     else:
        print("the number is less than yours")
     tries += 1
     n = eval(input("TYPE A NUMBER"))
if n == sentinel:
 print("GAME OVER")
elif n == nb:
 print("you have guessed the number!")
 print("congratulations")
elif tries == 4:
 print("Too many attempts")