alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# TODO-1: Crie uma função diferente chamada 'decrypt' que recebe o 'text' e 'shift' como entradas.
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"

    # TODO-2: Dentro da função 'descriptografar', desloque cada letra do 'texto' *para trás* no alfabeto pela quantidade de deslocamento e imprima o texto #
    # descriptografado.
    # por exemplo.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "olá"
    # print output: "O texto decodificado é hello


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# TODO-3: Verifique se o usuário deseja criptografar ou descriptografar a mensagem verificando a variável 'direction'. Em seguida, chame a função correta com base nessa variável 'drection'. Você deve ser capaz de testar o código para criptografar *E* descriptografar uma mensagem.

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)