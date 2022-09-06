################### Scope ####################

# game_level = 3
# def create_enemy():
#   enemies = ["Skeleton", "Zombie","Alien"]
#   if game_level < 5:
#     new_enemy = enemies[0]

#   print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
