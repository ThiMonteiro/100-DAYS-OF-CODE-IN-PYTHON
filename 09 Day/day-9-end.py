##Python Dictionaries
##Dicionários Python

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

#Recuperando itens do dicionário.
#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adicionando novos itens ao dicionário.
#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."


#Cria um dicionário vazio.
#Create an empty dictionary.
empty_dictionary = {}

#Limpar um dicionário existente
#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)


#Editar um item em um dicionário
#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)


#Percorrer um dicionário
#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################


#Aninhamento
#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Aninhando uma lista em um dicionário
#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Aninhamento de dicionário em um dicionário
#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Aninhamento de dicionários em listas
#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]