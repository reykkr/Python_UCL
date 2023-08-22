year1 = int(input("Enter year 1: "))
year2 = int(input("Enter year 2: "))
for i in range (year1, year2 +1):
    if (i % 4 == 0 and i % 100 != 0):
        print(i, end=" ")