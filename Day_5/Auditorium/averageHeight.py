""""
Instructions
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
"""

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sumar = 0
for i in student_heights:
  sumar = sumar + i
print(f"total height = {sumar}")

numOfStudents = 0
for b in student_heights:
  numOfStudents = numOfStudents + 1
print(f"number of students = {numOfStudents}")

avgHeight = 0
for c in student_heights:
  avgHeight = round(sumar / numOfStudents)
print(f"average height = {avgHeight}")

# Write your code below this row 👇
