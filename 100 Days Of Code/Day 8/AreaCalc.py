import math


def paintCalc(height, width, cover):
    cal = math.ceil((height * width) / cover)
    print(f"You'll need {cal} cans of paint.")


testH = int(input("Height of wall: "))
testW = int(input("Width of wall: "))
coverage = 5
paintCalc(height=testH, width=testW, cover=coverage)
