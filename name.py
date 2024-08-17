student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for students in student_scores:
    if student_scores[students] >= 91 and student_scores[students] <= 100:
        student_grades[students] = "Outstanding"
    if student_scores[students] >= 81 and student_scores[students] <= 90:
        student_grades[students] = "Exceeds Expectations"
    if student_scores[students] >= 71 and student_scores[students] <= 80:
        student_grades[students] = "Acceptable"
    if student_scores[students] <= 70:
        student_grades[students] = "Fail"

print(student_grades)