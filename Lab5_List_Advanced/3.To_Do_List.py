sorted_list_of_importance = [0] * 10
command = input()

while not command == "End":
    importance, note = command.split("-")
    current_index = int(importance) - 1
    sorted_list_of_importance[current_index] = note
    command = input()

print([i for i in sorted_list_of_importance if not i == 0])


