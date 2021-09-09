# 12:10

destinations = input()
changed_str = destinations
command = input()

while not command == "Travel":
    command = command.split(":")
    instruction = command[0]

    if instruction == "Add Stop":
        index = int(command[1])
        string = command[2]
        if index < (len(changed_str)):
            changed_str = changed_str[:index] + string + changed_str[index:]
            print(changed_str)
        else:
            print(changed_str)
    elif instruction == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < (len(changed_str)) and end_index < (len(changed_str)):
            changed_str = changed_str[:start_index] + changed_str[end_index + 1:]
            print(changed_str)
        else:
            print(changed_str)
    elif instruction == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in destinations:
            changed_str = changed_str.replace(old_string, new_string)
            print(changed_str)
        else:
            print(changed_str)

    command = input()

print(f"Ready for world tour! Planned stops: {changed_str}")

# 12:35 -> judge -> 33/100???
# 12:53 -> judge -> 66/100
