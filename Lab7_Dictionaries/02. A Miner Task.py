command = input()

resources_list = []
resources_dict = {}

while not command == "stop":
    key = command
    if key not in resources_dict:
        resources_dict[key] = 0
    value = int(input())
    resources_dict[key] += value

    command = input()

for key, value in resources_dict.items():
    print(f"{key} -> {value}")