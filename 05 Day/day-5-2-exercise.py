# 🚨 Don't change the code below 👇
# 🚨 Não altere o código abaixo 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
# 🚨 Não altere o código acima 👆

#Write your code below this row 👇
#Escreva seu código abaixo desta linha 👇

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in class in: {highest_score}")
