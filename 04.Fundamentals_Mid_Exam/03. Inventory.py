items = input().split(", ")
command = input().split(" - ")

while not command[0] == "Craft!":
    if command[0] == "Collect":
        if not command[1] in items:
            items.append(command[1])
    elif command[0] == "Drop":
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == "Combine Items":
        old_item, new_item = command[1].split(":")
        if old_item in items:
            new_item_index = items.index(old_item) + 1
            items.insert(new_item_index, new_item)
    elif command[0] == "Renew":
        if command[1] in items:
            items.append(command[1])
            items.remove(command[1])
    command = input().split(" - ")
print(", ".join(items))
