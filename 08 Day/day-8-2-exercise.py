#Write your code below this line 👇
#Escreva seu código abaixo desta linha 👇
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


#Escreva seu código acima desta linha 👆
#Write your code above this line 👆


#NÃO altere nenhum dos códigos abaixo👇
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



