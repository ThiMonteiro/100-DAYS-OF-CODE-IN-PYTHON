from random import randint
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Função para verificar o palpite do usuário em relação à resposta real.
# Funtion to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """ Checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


# Faça a função para definir a dificuldade
# Make function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  print(logo)
  # Escolhendo um número aleatório entre 1 e 100
  # Choosing a random number betwen 1 and 100
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  answer = randint(1, 100)
  #print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  print(f"You have {turns} attempts remainig to guess the number.")

  # Deixe o usuário adivinhar um número.
  # Let the user guess a number.
  guess = 0
  while guess != answer:
    guess = int(input("Make a guess:"))
    turns = check_answer(guess, answer, turns)

  # Acompanhe o número de voltas e reduza em 1 se errar.
  # Track the number of turns and reduce by 1 if they get ir wrong.
  if turns == 0:
    print("You've run out of guesses, you lose.")
  elif guess != answer:
    print("Guess again.")

# Repita a funcionalidade de adivinhação se eles errarem.
# Repeat the guessing functionality if they get it wrong.
game()
