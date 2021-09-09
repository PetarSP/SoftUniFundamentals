raw_str = input()  # act_key_pattern = r"\b[A-Za-z0-9]\b"

command = input()

while not command == "Generate":
    instructions = command.split(">>>")
    if instructions[0] == "Contains":
        if instructions[1] in raw_str:
            print(f"{raw_str} contains {instructions[1]}")
        else:
            print("Substring not found!")
    elif instructions[0] == "Flip":
        if instructions[1] == "Upper":
            new_str = raw_str[int(instructions[2]):int(instructions[3])].upper()
            last_str = f"{raw_str[0:int(instructions[2])]}{new_str}{raw_str[int(instructions[3]):]}"
            raw_str = last_str
            print(raw_str)
        elif instructions[1] == "Lower":
            new_str = raw_str[int(instructions[2]):int(instructions[3])].lower()
            last_str = f"{raw_str[0:int(instructions[2])]}{new_str}{raw_str[int(instructions[3]):]}"
            raw_str = last_str
            print(raw_str)
    elif instructions[0] == "Slice":
        new_str = raw_str[:int(instructions[1])]+raw_str[int(instructions[2]):]
        print(new_str)
        raw_str = new_str

    command = input()

print(f"Your activation key is: {raw_str}")
