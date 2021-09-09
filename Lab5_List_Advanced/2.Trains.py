wagons = int(input())

empty_wagons = [0 for wagon in range(wagons)]

command = input().split()
while not command[0] == "End":
    if command[0] == "add":
        empty_wagons[-1] += int(command[1])
    elif command[0] == "insert":
        empty_wagons[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        empty_wagons[int(command[1])] -= int(command[2])
    command = input().split()

print(empty_wagons)
