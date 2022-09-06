alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"

        # TODO-3: O que acontece se o usuário digitar um número/símbolo/espaço?
        # Você pode corrigir o código para manter o número/símbolo/espaço quando o texto é codificado/decodificado?
        # por exemplo. start_text = "me encontre às 3"
        # end_text = "•••• •• •• 3"

    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
# TODO-1: Importe e imprima o logotipo do art.py quando o programa iniciar.
from art import logo

print(logo)

# TODO-4: Você pode descobrir uma maneira de perguntar ao usuário se ele deseja reiniciar o programa de cifra?
# por exemplo. Digite 'sim' se quiser ir novamente. Caso contrário, digite 'não'.
# Se eles digitarem 'sim', então peça-lhes a direção/texto/deslocamento novamente e chame a função caesar() novamente?
# Dica: Tente criar um loop while que continue a executar o programa se o usuário digitar 'sim'.

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).

    # TODO-2: E se o usuário inserir um deslocamento maior que o número de letras do alfabeto?
    # Tente executar o programa e inserir um número de turno de 45.
    # Adicione algum código para que o programa continue funcionando mesmo que o usuário insira um número de turno maior que 26.
    # Dica: Pense em como você pode usar o módulo (%).
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'Yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")