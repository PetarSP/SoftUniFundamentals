list_of_gifts = input().split()

# ['"{gift1}', '{gift2}', '{gift3}…', '{giftn}"']

full_command = input().split()
command_type = full_command[0]
gift_type = full_command[1]
# •	"OutOfStock {gift}" // "Required {gift} {index}" // "JustInCase {gift}" // "No Money"

while not command_type == "No" and not gift_type == "Money":

    if command_type == "OutOfStock":
        if gift_type in list_of_gifts:
            while gift_type in list_of_gifts:
                gift_type_index = list_of_gifts.index(gift_type)
                list_of_gifts[gift_type_index] = None
            # index_gift_type = list_of_gifts.index(gift_type)
            # list_of_gifts.pop(index_gift_type)
    elif command_type == "Required":
        gift_index = full_command[2]
        if int(gift_index) in range(len(list_of_gifts) - 1):
            list_of_gifts[int(gift_index)] = gift_type
    elif command_type == "JustInCase":
        list_of_gifts[-1] = gift_type
    full_command = input().split()
    command_type = full_command[0]
    gift_type = full_command[1]

for i in list_of_gifts:
    while i is None:
        list_of_gifts.remove(i)
        break

new_list = " ".join(list_of_gifts)
print(new_list, end="")









# correct way
#
# gifts = input().split()
# command = input()
#
# while not command == "No Money":
#     command = command.split()
#     if "OutOfStock" in command:
#         for i in range(len(gifts)):
#             if command[1] in gifts[i]:
#                 gifts[i] = "None"
#     elif "Required" in command:
#         for i in range(len(gifts)):
#             if i == int(command[2]):
#                 gifts[i] = command[1]
#     elif "JustInCase" in command:
#         gifts[-1] = command[1]
#     command = input()
# while "None" in gifts:
#     gifts.remove("None")
# for i in gifts:
#     print(i, end=" ")