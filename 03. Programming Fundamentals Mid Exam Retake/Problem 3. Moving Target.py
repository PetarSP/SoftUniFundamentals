# 15:30
targets = input().split()
int_targets = [int(target) for target in targets]

command = input()

while not command == "End":
    command = command.split()
    instruction = command[0]
    index = int(command[1])

    if instruction == "Shoot":
        power = int(command[2])
        if index < len(int_targets):
            int_targets[index] -= power
            if int_targets[index] == 0 or int_targets[index] < 0:
                int_targets.remove(int_targets[index])

    elif instruction == "Add":
        value = int(command[2])
        if index < len(int_targets):
            int_targets.insert(index, value)
        else:
            print(f"Invalid placement!")

    elif instruction == "Strike":
        radius = int(command[2])
        if index < len(int_targets) and (index + radius) < len(int_targets) and 0 <= (index - radius) < len(
                int_targets):
            for el_index in range(len(int_targets)):
                if el_index in range((index - radius), (index + radius)):
                    int_targets = int_targets[:(index - radius)]+int_targets[((index+1) + radius):]
                    break
        else:
            print(f"Strike missed!")


    command = input()

str_targets = [str(target) for target in int_targets]
print(f"{'|'.join(str_targets)}")