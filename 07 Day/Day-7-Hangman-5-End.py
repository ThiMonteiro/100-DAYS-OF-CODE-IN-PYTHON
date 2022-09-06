# Step 5
# Passo 5

from replit import clear
import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
# TODO-1: - Atualize a lista de palavras para usar a 'word_list' de hangman_words.py
# Delete esta linha: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# TODO-3: - Importe o logotipo do hangman_art.py e imprima-o no início do jogo.
from hangman_art import logo

print(logo)

# Testing code
# Código de teste
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
# Criar espaços em branco
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    # TODO-4: - Se o usuário digitou uma letra que já adivinhou, imprima a letra e avise.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    # Verificar letra adivinhada
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    # Verifique se o usuário está errado.
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    # Junte todos os elementos da lista e transforme em uma String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    # Verifica se o usuário tem todas as letras.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages

    print(stages[lives])