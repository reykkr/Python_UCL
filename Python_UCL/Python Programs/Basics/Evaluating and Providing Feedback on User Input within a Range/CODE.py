a = eval(input("enter a number between 5 and 10"))
if a < 5:
    print("too low")
elif 5 <= a <= 10:
    print("valid number")
elif a > 10:
    print("too high")