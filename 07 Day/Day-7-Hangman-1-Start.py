#Step 1

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Escolha aleatoriamente uma palavra da lista_palavras e atribua-a a uma variável chamada palavra_escolhida.
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chose_word = random.choice(word_list)

#TODO-2 - Peça ao usuário que adivinhe uma letra e atribua sua resposta a uma variável chamada guess. Faça adivinhar minúsculas.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Verifique se a letra que o usuário adivinhou é uma das letras da palavra escolhida.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chose_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")
