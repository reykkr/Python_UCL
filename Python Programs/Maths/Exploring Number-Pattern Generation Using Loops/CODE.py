n = eval(input("Enter a number: "))
star = '*'
for i in range(n):
    print(star)
    star += '*'
for i in range(n+1):
    for j in range(i):
        print('*', end='')
    print()