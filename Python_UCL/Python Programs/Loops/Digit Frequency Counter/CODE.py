n = eval(input("Enter the first number: "))
i = eval(input("Enter the second number: "))
m = n
sum  = 0
count = 0
if i//10:
    print("error the second input should be only 1 digit")
if m == i:
    print(i, "appears 1 time in", n)
else:
    for x in range (n):
        sum = m % 10
        m = m // 10
        if sum == i:
           count += 1
    print(i, "appears", count, "times in", n)