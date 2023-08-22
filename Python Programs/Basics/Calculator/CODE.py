x = eval(input("enter the first number"))
y = eval(input("enter the second number"))

op=input("Enter Operator (+,-,*,/) : ")

if op=="+":
    z=x+y
    print("Addition = ", z)
elif op=="*":
     z=x*y
     print("Multiplication = ", z)
elif op=="-":
     if(x>y):
         z=x-y
     else:
         z=y-x
     print("substraction = ", z)
elif op=="/":
     z=x/y
     print("Division = ", z)
else:
    print("Invalid operator")

title & summary for it