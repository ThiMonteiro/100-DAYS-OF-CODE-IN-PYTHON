# Passo 2
# Step 2

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Código de teste
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Cria uma lista vazia chamada display.
# Para cada letra na palavra_escolhida, adicione um "_" a 'exibir'.
# Então, se a palavra escolhida for "maçã", a exibição deve ser ["_", "_", "_", "_", "_"] com 5 "_" representando cada letra a ser adivinhada.

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

# TODO-2: - Percorrer cada posição na palavra escolhida;
# Se a letra nessa posição corresponder a 'adivinha', revele essa letra no visor nessa posição.
# por exemplo. Se o usuário adivinhou "p" e a palavra escolhida foi "maçã", a exibição deve ser ["_", "p", "p", "_", "_"

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for positition in range(word_length):
    letter = chosen_word[positition]
    if letter == guess:
        display[positition] = letter

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# TODO-3: - Imprima 'display' e você deverá ver a letra adivinhada na posição correta e todas as outras letras substituídas por "_".
# Dica - Não se preocupe em fazer o usuário adivinhar a próxima letra. Vamos resolver isso na etapa 3.