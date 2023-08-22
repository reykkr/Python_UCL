n = eval(input("Write a number: "))
sum = 0
if n > 0:
    for i in range(1, n):
        if n % i == 0:
            sum += i
else:
    for i in range(-1, n, -1):
        if n % -i == 0:
            sum += i
if sum == n:
    print("yes")
else:
    print("no")