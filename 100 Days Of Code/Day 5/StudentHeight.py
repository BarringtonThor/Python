student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

average = student_heights[n] / int(len(student_heights))
print(average)

total_height = 0
for height in student_heights:
    total_height += height

number_of_students = 0
for student in student_heights:
    number_of_students += 1
