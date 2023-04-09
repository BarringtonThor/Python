import random

fruits = ["Apple", "Cherry", "Orange"]

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

numItems = len(names)

randomChoice = random.randint(0, numItems - 1)
personWhoWillPay = names[randomChoice]
print(personWhoWillPay + " is going to buy the meal today.")

# OR

personWhoWillPay = random.choice(names)
print(personWhoWillPay + " is going to buy the meal today.")
