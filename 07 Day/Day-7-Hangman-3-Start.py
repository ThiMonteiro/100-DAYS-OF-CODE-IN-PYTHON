# Step 3
# Etapa 3

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Código de teste
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Criar espaços em branco
# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# TODO-1: - Use um loop while para deixar o usuário adivinhar novamente. O loop só deve parar quando o usuário adivinhar todas as letras da palavra escolhida e 'display' não tiver mais espaços em branco ("_"). Então você pode dizer ao usuário que eles ganharam.
# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Verificar letra adivinhada
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")
