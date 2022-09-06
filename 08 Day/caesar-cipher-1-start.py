alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# TODO-1: Crie uma função chamada 'encrypt' que recebe o 'texto' e o 'shift' como entradas.
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encode text is {cipher_text}")

    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    # TODO-2: Dentro da função 'encrypt', desloque cada letra do 'texto' para frente no alfabeto pela quantidade de deslocamento e imprima o texto
    # criptografado.
    # por exemplo.
    # plain_text = "olá"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "O texto codificado é mjqqt"
    ##HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    ##🐛Alerta de bug: O que acontece se você tentar codificar a palavra 'civilização'?🐛


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# TODO-3: Chame a função encrypt e passe as entradas do usuário. Você deve ser capaz de testar o código e criptografar uma mensagem.
encrypt(plain_text=text, shift_amount=shift)
