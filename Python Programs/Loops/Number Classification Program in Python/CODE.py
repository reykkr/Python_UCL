n = input("enter a number")
while n != "q":
    if eval(n) % 1 == 0:
        if eval(n) % 2 == 0:
            print("you chose an even number")
        else:
            print("you chose an odd number")
    else:
        print("please enter an int")
    n = input("enter a new number")
print("bye")
