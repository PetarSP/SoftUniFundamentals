numbers = input().split()

command = input()

while not command == "Finish":
    command = command.split()
    if command[0] == "Add":
        numbers.append(command[1])
    if command[0] == "Remove":
        if command[1] in numbers:
            numbers.remove(command[1])
    if command[0] == "Replace":
        if command[1] in numbers:
            index = numbers.index(command[1])
            numbers.insert(index, command[2])
            numbers.remove(command[1])
    if command[0] == "Collapse":
        for num in numbers:
            if num <= command[1]:
                numbers.remove(num)

    command = input()
print(" ".join(numbers))