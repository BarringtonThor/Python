import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
userChoice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if userChoice >= 3 or userChoice < 0:
    print("YOU TYPED AN INVALID NUMBER, YOU LOSE!")
else:
    print(images[userChoice])
    cpuChoice = random.randint(0, 2)
    print("Computer chose: ")
    print(images[cpuChoice])

    if userChoice == 0 and cpuChoice == 2:
        print("You Win!")
    elif cpuChoice == 0 and userChoice == 2:
        print("You Lose!")
    elif cpuChoice > userChoice:
        print("You Lose!")
    elif userChoice > cpuChoice:
        print("You Win!")
    elif cpuChoice == userChoice:
        print("It's a Draw!")
