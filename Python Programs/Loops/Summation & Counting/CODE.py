# Summation

n = eval(input("enter a number"))
count = 0
sum = 0
while count <= n and sum < 100:
    sum += count
    count += 1
    print(sum)
print(sum)

# Counting

n = eval(input("enter a nb"))
count = 0
sum = 0
while sum <= n:
   if count != 10:
       sum += count
   count += 1
   print(sum)
print("hi \' how are you")