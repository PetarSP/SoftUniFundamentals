num_of_commands = int(input())

register_users = {}

while not num_of_commands == 0:
    command = input().split(" ")
    command_type = command[0]
    username = command[1]
    if command_type == "register":
        license_plate = command[2]
        if username in register_users:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            register_users[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    elif command_type == "unregister":
        if username not in register_users:
            print(f"ERROR: user {username} not found")
        else:
            del register_users[username]
            print(f"{username} unregistered successfully")

    num_of_commands -= 1

for username, license_plate in register_users.items():
    print(f"{username} => {license_plate}")