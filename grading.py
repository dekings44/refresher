print('Welcome to Grading Program')

student_scores = {
    'Kingsley': 99,
    'Chisom': 90,
    'Chizurum': 85,
    'Peter': 49,
    'Chinaza': 65,
    'Lawrence': 76
}


for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_scores[student] = "Outstanding"
    elif score > 80:
        student_scores[student] = "Exceeds Expectation"

    elif score > 70:
        student_scores[student] = "Acceptable"
    else:
        student_scores[student] = "Fail"

print(student_scores)