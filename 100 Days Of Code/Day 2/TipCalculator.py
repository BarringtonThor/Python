print("Welcome to the tip Calculator!")
total = float(input("What was the total bill? $"))
percent = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
billWithTip = percent / 100 * total + total
billPerPerson = billWithTip / people
finalAmount = round(billPerPerson, 2)
finalAmount = "{:.2f}".format(billPerPerson)
print(f"Each person should pay: ${finalAmount}")
