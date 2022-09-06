# 🚨 Don't change the code below 👇
# 🚨 Não altere o código abaixo 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
# 🚨 Não altere o código acima 👆

#Write your code below this line 👇
#Escreva seu código abaixo desta linha 👇

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year.")
  else:
    print("Leap Year.")
else:
  print("Not leap year")
