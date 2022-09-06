# 🚨 Não altere o código abaixo 👇
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
# 🚨 Não altere o código acima 👆

#Write your code below this row 👇
#Escreva seu código abaixo desta linha 👇

horizonal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizonal - 1] = "X"

#Write your code above this row 👆
#Escreva seu código acima desta linha 👆

# 🚨 Não altere o código abaixo 👇
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
