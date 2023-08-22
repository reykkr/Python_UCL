n = int(input("Enter a number: "))
first = 0
second = 1
if n <= 0:
    print("Number should be more than 0")
elif n == 1:
    print(first, end=' ')
elif n > 1:
    print(first, end=' ')
    print(second, end=' ')
    i = 2
    while i < n:
        fib_sum = first + second
        first = second
        second = fib_sum
        print(fib_sum, end=' ')
        i += 1