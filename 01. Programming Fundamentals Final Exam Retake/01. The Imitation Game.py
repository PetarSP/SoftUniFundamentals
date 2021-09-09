# Start -> 12:30

encrypted_message = input()
command = input()

while not command == "Decode":
    command = command.split("|")
    instruction = command[0]

    if instruction == "Move":
        num_letters = int(command[1])
        encrypted_message = encrypted_message[num_letters:] + encrypted_message[:num_letters]
    elif instruction == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif instruction == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring,replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")

# End -> 12:43