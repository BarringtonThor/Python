import random

fruits = ["Apple", "Cherry", "Orange"]

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
names = random.randint(0, 10)

print(names)
