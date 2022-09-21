from time import sleep

text_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
           'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
           'I': '..','J': '.---', 'K': '-.-', 'L': '.-..',
           'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
           'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
           'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
           'Y': '-.--', 'Z': '--..',

           '0': '-----',    '1': '.----',   '2': '..---',   '3': '...--',
           '4': '....-',    '5': '.....',   '6': '-....',   '7': '--...',
           '8': '---..',    '9': '----.',   ' ': '\n'}


while True:
    try:
        text = str(input('Digite seu texto: ')).upper()
        morse = ' '

        for char in text:
            sleep(1)
            morse = text_morse[char]
            if char != " ":
                print(f'{char} = {morse}')
            else:
                print(morse)

    except KeyError as ke:
        print('-'*40)
        print(f'{ke} = Caractere não reconhecido')
        print("Tente novamente!")
        print('-'*40)

    except KeyboardInterrupt as kbi:
        print('Você parou o programa. Volte sempre = )!')


    else:
        sleep(0.5)
        print('-' * 40)
        print('Tradução feita com sucesso!')
        opition = str(input('Deseja traduzir outro texto? [S/N] ')).upper()
        print('-' * 40)

        if opition == 'S':
            print('-'*40)
            print('Escreva seu novo texto:')
            print('-'*40)

        else:
            print('-'*40)
            print('Saindo do programa. Volte sempre = )!')
            print('-'*40)
            sleep(1)
            break


