initial_health = 100
initial_bitcoin = 0

dungeons_rooms = input().split("|")
current_room = 0
for each_room in dungeons_rooms:
    command = each_room.split()
    current_room += 1
    if command[0] == "potion":
        if not initial_health + int(command[1]) > 100:
            initial_health += int(command[1])
            print(f"You healed for {command[1]} hp.")
            print(f"Current health: {initial_health} hp.")
        else:
            print(f"You healed for {100 - initial_health} hp.")
            initial_health = 100
            print(f"Current health: {initial_health} hp.")
    elif command[0] == "chest":
        initial_bitcoin += int(command[1])
        print(f"You found {command[1]} bitcoins.")
    else:
        initial_health -= int(command[1])
        if not initial_health <= 0:
            print(f"You slayed {command[0]}.")
        else:
            print(f"You died! Killed by {command[0]}.")
            print(f"Best room: {current_room}")
            exit()

print(f"You've made it!\nBitcoins: {initial_bitcoin}\nHealth: {initial_health}")
