# 🚨 Não altere o código abaixo 👇
# 🚨 Don't change the code below 👇

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
# 🚨 Não altere o código acima 👆

# Write your code below this row 👇
# Escreva seu código abaixo desta linha 👇

total_heigths = 0
for heights in student_heights:
    total_heigths += heights

number_of_students = 0
for student in student_heights:
    number_of_students += 1

average = round(total_heigths / number_of_students)
print(average)
