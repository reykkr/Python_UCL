n = eval(input("enter a number"))
m = n
count = 1
while n // 10:
   if n > 0:
    count += 1
    n = n // 10
   elif n < 0:
    count += 1
    n = n // 10
   elif n == 0:
    count = 1
print(m , "has", count , "digits")

#Another way

#if n < 0:
#   n = n * -1
#if n != 0:
#   while n>0:
#        n = n // 10
#        count += 1