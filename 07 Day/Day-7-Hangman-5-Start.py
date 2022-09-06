# Step 5
# Passo 5

import random

# TODO-1: - Atualize a lista de palavras para usar a 'word_list' de hangman_words.py
# Delete esta linha: word_list = ["ardvark", "baboon", "camel"]
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# TODO-3: - Importe o logotipo do hangman_art.py e imprima-o no início do jogo.
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

# Código de teste
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Criar espaços em branco
# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # TODO-4: - Se o usuário digitou uma letra que já adivinhou, imprima a letra e avise.
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    # Verificar letra adivinhada
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Verifique se o usuário está errado.
    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - Se a letra não estiver na palavra escolhida, imprima a letra e avise que não está na palavra.
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Junte todos os elementos da lista e transforme em uma String.
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Verifica se o usuário tem todas as letras.
    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-2: - Importe os estágios do hangman_art.py e faça com que este erro desapareça.
    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])