shopping_list = input().split()

empty_dict = {}

for index in range(0, len(shopping_list), 2):
    key = shopping_list[index]
    value = int(shopping_list[index + 1])
    empty_dict[key] = value

print(empty_dict)
