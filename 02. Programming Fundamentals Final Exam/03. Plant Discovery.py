# 13:40

number_of_plants = int(input())

plants_dict = {}

for _ in range(number_of_plants):
    plant, rarity = input().split("<->")
    rarity = int(rarity)

    if plant not in plants_dict:
        plants_dict[plant] = {"rarity": rarity, "rating": []}
    else:
        plants_dict[plant] = {"rarity": rarity, "rating": []}

command = input()

while not command == "Exhibition":
    command = command.split(": ")
    instruction = command[0]
    action = command[1].split(" - ")
    plant = action[0]

    if instruction == "Rate":
        rating = int(action[1])
        plants_dict[plant]["rating"].append(rating)

    elif instruction == "Update":
        new_rarity = int(action[1])
        plants_dict[plant]["rarity"] = new_rarity
    elif instruction == "Reset":
        plants_dict[plant]["rating"].clear()

    command = input()

for key, data in plants_dict.items():
    if data["rating"]:
        avg_rating = sum(data["rating"])/len(data["rating"])
        data["rating"] = avg_rating
    else:
        avg_rating = 0
        data["rating"] = avg_rating

sorted_plant_dict = sorted(plants_dict.items(), key=lambda x: (x[1]["rarity"], x[1]["rating"]),reverse= True)
a = 5