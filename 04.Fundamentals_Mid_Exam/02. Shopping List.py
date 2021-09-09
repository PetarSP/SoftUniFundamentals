def is_in_grocery_list(item: str, current_list: list):
    if item in current_list:
        return True
    return False


grocery_list = input().split("!")
data = input()
while not data == "Go Shopping!":
    data = data.split()
    if data[0] == "Urgent" and not is_in_grocery_list(data[1], grocery_list):
        grocery_list.insert(0, data[1])
    elif data[0] == "Unnecessary" and is_in_grocery_list(data[1], grocery_list):
        grocery_list.remove(data[1])
    elif data[0] == "Correct" and is_in_grocery_list(data[1], grocery_list):
        new_item_index = grocery_list.index(data[1])
        grocery_list[new_item_index] = data[2]
    elif data[0] == "Rearrange" and is_in_grocery_list(data[1], grocery_list):
        grocery_list.remove(data[1])
        grocery_list.append(data[1])
    data = input()

print(", ".join(grocery_list))
