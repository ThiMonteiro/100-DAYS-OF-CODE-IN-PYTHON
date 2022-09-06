programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

# print(programming_dictionary["Function"])

# Adicionando novos itens ao dicionário.
# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Cria um dicionário vazio.
# Create an empty dictionary.
empty_dictionary = {}

# Limpe um dicionário existente.
# Wipe an existin dictionary.
# programming_dictionary = {}
# print(programming_dictionary)


# Edita um item em um dicionário
# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)


# Percorrer um dicionário
# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
