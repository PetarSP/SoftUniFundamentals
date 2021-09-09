initial_loot = input().split("|")

command = input()

while not command == "Yohoho!":
    command = command.split()
    instruction = command[0]

    if instruction == "Loot":
        for el in command[1:]:
            if el in initial_loot:
                pass
            else:
                initial_loot.insert(0,el)

    elif instruction == "Drop":
        index = int(command[1])
        if index < len(initial_loot):
            current_element = initial_loot.pop(index)
            initial_loot.append(current_element)
        else:
            pass
    elif instruction == "Steal":
        count = int(command[1])
        if count < len(initial_loot):
            items_left = initial_loot[-count:]
            print(f"{', '.join(items_left)}")
            initial_loot = initial_loot[:-count]

    command = input()

total_gain = 0
for el in initial_loot:
    total_gain += len(el)

average_gain = total_gain / len(initial_loot)
print(f"Average treasure gain: {average_gain:.2f} pirate credits.")