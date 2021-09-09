command = input()

records = {}
while not command == "Results":
    command = command.split(":")
    instruction = command[0]

    if instruction == "Add":
        person_name = command[1]
        health = int(command[2])
        energy = int(command[3])
        if person_name not in records:
            records[person_name] = {"health": health, "energy": energy}
        else:
            records[person_name]["health"] += health

    elif instruction == "Attack":
        attacker_name = command[1]
        defender_name = command[2]
        damage = int(command[3])
        if attacker_name in records and defender_name in records:
            records[defender_name]["health"] -= damage
            records[attacker_name]["energy"] -= 1
            if records[defender_name]["health"] <= 0:
                del records[defender_name]
                print(f"{defender_name} was disqualified!")
            if records[attacker_name]["energy"] <= 0:
                del records[attacker_name]
                print(f"{attacker_name} was disqualified!")

    elif instruction == "Delete":
        user_name = command[1]
        if user_name in records:
            del records[user_name]
        if user_name == "All":
            records.clear()

    command = input()

print(f"People count: {len(records)}")

sorted_records = sorted(records.items(), key=lambda x: (-x[1]["health"], x[0]))

for name, data in sorted_records:
    print(f"{name} - {data['health']} - {data['energy']}")