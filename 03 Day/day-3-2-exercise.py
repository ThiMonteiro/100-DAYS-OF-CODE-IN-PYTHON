# 🚨 Don't change the code below 👇
# 🚨 Não altere o código abaixo 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
# 🚨 Não altere o código acima 👆

#Write your code below this line 👇
#Escreva seu código abaixo desta linha 👇

bmi = round(weight / height ** 2)

if bmi < 18.5:
  print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your bmi is {bmi}, your are overweight")
elif bmi < 35:
  print(f"Your bmi is {bmi}, you are obese.")
else:
  print(f"Your bmi is {bmi}, you are clinically obese.")
