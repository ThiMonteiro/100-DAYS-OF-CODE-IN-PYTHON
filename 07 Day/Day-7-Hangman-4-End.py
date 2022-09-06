# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

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
    # Verificar letra adivinhada
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Posição atual: {posição}\n Letra atual: {letra}\n Letra adivinhada: {adivinha}")
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # TODO-2: - Se o palpite não for uma letra na palavra escolhida,
    # Então reduza 'vidas' em 1.
    # Se as vidas chegarem a 0, o jogo deve parar e exibir "Você perde".

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
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

    # TODO-3: - imprimir a arte ASCII de 'stages' que corresponde ao número atual de 'lives' que o usuário tem restantes.
    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])