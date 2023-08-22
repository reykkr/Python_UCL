x1 = eval(input("enter the horizontal value for point 1"))
y1 = eval(input("enter the vertical value for point 1"))
x2 = eval(input("enter the horizontal value for point 2"))
y2 = eval(input("enter the vertical value for point 2"))

distance = (x2 - x1)**2 + (y2 - y1)**2
sqrt = distance * 0.5
if sqrt > 5:
   print("far from each other")
else:
    print("close to each other")