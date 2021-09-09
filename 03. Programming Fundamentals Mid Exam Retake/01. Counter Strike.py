# 13:50

initial_energy = int(input())

command = input()

battle_wins = 0
while True:
    if command == "End of battle":
        print(f"Won battles: {battle_wins}. Energy left: {initial_energy}")
        break
    distance = int(command)
    if initial_energy < distance:
        print(f"Not enough energy! Game ends with {battle_wins} won battles and {initial_energy} energy")
        break
    initial_energy -= distance
    battle_wins += 1

    if battle_wins % 3 == 0:
        initial_energy += battle_wins
    command = input()

# 14:15