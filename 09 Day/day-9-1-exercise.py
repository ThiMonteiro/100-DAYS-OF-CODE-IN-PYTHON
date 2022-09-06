student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
# 🚨 Não altere o código acima 👆

# TODO-1: Create an empty dictionary called student_grades.
# TODO-1: Crie um dicionário vazio chamado student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
# TODO-2: Escreva seu código abaixo para adicionar as notas a student_grades.👇

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# 🚨 Não altere o código abaixo 👇
# 🚨 Don't change the code below 👇
print(student_grades)

