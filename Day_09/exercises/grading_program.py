student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for value in student_scores:
    student_grades[value] = student_scores[value]
    if student_grades[value] <= 70:
        print(f"{value}'s Grade = Fail")
    elif student_grades[value] <= 80:
        print(f"{value}'s Grade = Acceptable")
    elif student_grades[value] <= 90:
        print(f"{value}'s Grade = Exceeds Expectations")
    elif student_grades[value] > 91:
        print(f"{value}'s Grade = Outstanding" )