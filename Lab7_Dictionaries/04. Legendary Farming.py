def legendary_item_reveal(key_materials: dict):
    for each_key, each_value in key_materials.items():
        if key_materials[each_key] >= 250:
            return True, each_key, each_value


any_material = []

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

while not legendary_item_reveal(key_materials):
    any_material = input().split()

    for index in range(0, len(any_material), 2):
        value = any_material[index]
        key = any_material[index + 1].lower()
        if key_materials["shards"] >= 250 or key_materials["fragments"] >= 250 or key_materials["motes"] >= 250:
            break
        elif key == "shards" or key == "fragments" or key == "motes":
            if key not in key_materials:
                key_materials[key] = 0
            key_materials[key] += int(value)
        else:
            if key not in junk:
                junk[key] = 0
            junk[key] += int(value)

if legendary_item_reveal(key_materials)[1] == "fragments":
    key_materials["fragments"] -= 250
    print("Valanyr obtained!")
elif legendary_item_reveal(key_materials)[1] == "shards":
    key_materials["shards"] -= 250
    print("Shadowmourne obtained!")
else:
    key_materials["motes"] -= 250
    print("Dragonwrath obtained!")
sorted_key_materials = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
for key, value in sorted_key_materials:
    print(f"{key}: {value}")
sorted_junk = sorted(junk.items(), key=lambda x: x[0])
for key, value in sorted_junk:
    print(f"{key}: {value}")
