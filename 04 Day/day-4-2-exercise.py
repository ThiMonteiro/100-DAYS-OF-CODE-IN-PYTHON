import random
# Método de string dividida
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# 🚨 Não altere o código acima 👆


#Write your code below this line 👇
# Obtém o número total de itens na lista.
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " Is going to buy the meal today.")