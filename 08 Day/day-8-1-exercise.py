#Escreva seu código abaixo desta linha 👇
#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
  area = height * width
  num_of_cans = math.ceil(area / cover)
  print(f"You'll need {num_of_cans} cans of paint.")

#Escreva seu código acima desta linha 👆
#Write your code above this line 👆

# Define a function called paint_calc() so that the code below works.
# Defina uma função chamada paint_calc() para que o código abaixo funcione.

# 🚨 Não altere o código abaixo 👇
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


