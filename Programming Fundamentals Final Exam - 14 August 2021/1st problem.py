user_name = input()

command = input()

while not command == "Sign up":
    command = command.split()
    instruction = command[0]

    if instruction == "Case":
        lower_or_upper = command[1]
        if lower_or_upper == "lower":
            user_name = user_name.lower()
            print(user_name)
        else:
            user_name = user_name.upper()
            print(user_name)
    elif instruction == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(user_name) and end_index < len(user_name):
            sub_str = user_name[start_index:end_index +1]
            reversed_sub_str = sub_str[::-1]
            print(reversed_sub_str)
        elif end_index < 0:
            sub_str = user_name[start_index:end_index +1]
            reversed_sub_str = sub_str[::-1]
            print(reversed_sub_str)
        elif start_index > end_index:
            continue
        else:
            continue
    elif instruction == "Cut":
        sub_str = command[1]
        if sub_str in user_name:
            user_name = user_name.replace(sub_str, "")
            print(user_name)
        else:
            print(f"The word {user_name} doesn't contain {sub_str}.")
    elif instruction == "Replace":
        char = command[1]
        if char in user_name:
            user_name = user_name.replace(char, "*")
            print(user_name)
        else:
            continue
    elif instruction == "Check":
        char = command[1]
        if char in user_name:
            print(f"Valid")
        else:
            print(f"Your username must contain {char}.")


    command = input()
