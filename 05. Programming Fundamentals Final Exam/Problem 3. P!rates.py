command = input()

cities = {}
while not command == "Sail":
    city, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)
    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
    command = input()

command = input()

while not command == "End":
    command = command.split("=>")
    event = command[0]
    city = command[1]
    if event == "Plunder":
        population = int(command[2])
        gold = int(command[3])
        print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
        cities[city]["population"] -= population
        cities[city]["gold"] -= gold
        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")
    elif event == "Prosper":
        gold = int(command[2])
        if gold <= 0:
            print(f"Gold added cannot be a negative number!")
            command = input()
            continue
        else:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
    command = input()

print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
if not cities:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    sorted_dict = sorted(cities.items(), key=lambda kvp: (-kvp[1]["gold"], kvp[0]))
    for city, command in sorted_dict:
        print(f"{city} -> Population: {command['population']} citizens, Gold: {command['gold']} kg")
