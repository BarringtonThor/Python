year = int(input("Which year do you want to check? "))

if (year/4) and (year % 2 == 0):
    if (year/100) and (year % 2 == 0):
        if (year/400) and (year % 2 == 0):
            print(f"So the year {year} is a leap year!")
else:
    print(f"{year} is not a leap year!")
