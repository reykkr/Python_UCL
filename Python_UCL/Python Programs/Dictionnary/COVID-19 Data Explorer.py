covid_cases = { 'Cyprus' : [25, 1000, 2000],
                'France' : [100000, 123000, 240000],
                'UK' : [120000, 260000, 280000],}
print("1. Search by country" '\n'
      "2. Search by time stamp" '\n'
      "3. View all" '\n'
      "-------")
choice = int(input("Input your choice: "))
if choice < 1 or choice > 3:
    print("Choice not available")
if choice == 1:
    country_name = input("Enter the country name: ")
    if country_name in covid_cases:
        print(country_name, covid_cases[country_name][0], covid_cases[country_name][1], covid_cases[country_name][2])
elif choice == 2:
    timestamp = int(input("Enter time stamp: "))
    if timestamp < 1 or timestamp > 3:
        print("Invalid time stamp.")
    else:
        for i in covid_cases:
            print(i,":", covid_cases[i][timestamp - 1])
elif choice == 3:
    for i in covid_cases:
       print(i, ":", covid_cases[i][0], covid_cases[i][1], covid_cases[i][2],"; ", end="")