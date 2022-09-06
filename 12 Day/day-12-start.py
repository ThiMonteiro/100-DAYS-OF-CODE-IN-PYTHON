################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
  potion_strenght = 2
  print(potion_strenght)


drink_potion()
print(potion_strenght)

# Global Scope
player_health = 10

def drink_potion():
  potion_strenght = 2
  print(player_health)

drink_potion()
