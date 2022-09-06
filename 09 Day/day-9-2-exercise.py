travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above
# 🚨 NÃO altere o código acima

# TODO: Escreva a função que permitirá novos países
# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
# a ser adicionado ao travel_log. 👇

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


# 🚨 Não altere o código abaixo
# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
