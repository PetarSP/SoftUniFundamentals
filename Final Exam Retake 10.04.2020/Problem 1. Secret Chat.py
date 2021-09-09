# 11:20

concealed_message = input()
command = input()
result_str = ""
while not command == "Reveal":
    command = command.split(":|:")
    instr_type = command[0]

    if instr_type == "InsertSpace":
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif instr_type == "Reverse":
        substring = command[1]
        if substring in concealed_message:
            start_index = concealed_message.index(substring)
            end_index = (concealed_message.index(substring)) + len(substring)
            cut_str = concealed_message[:start_index] + concealed_message[end_index:]
            reversed_substring = "".join(list(reversed(substring)))
            concealed_message = cut_str + reversed_substring
            print(concealed_message)
        else:
            print("error")
    elif instr_type == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring,replacement)
            print(concealed_message)
    command = input()
print(f"You have a new text message: {concealed_message}")