

# left_half = []
# right_half = []
# new_list = []
# x = 0
#
# splitting_in_half = len(cards) // 2
#
# for j in cards:
#     if len(left_half) < splitting_in_half:
#         left_half += cards[x]
#         x += 1
#     elif len(right_half) < splitting_in_half and not x == len(cards):
#         right_half += cards[x]
#         x += 1
#
# while not num_faro_shuffle == 0:
#     for k in range(left_half):
#
#
#     num_faro_shuffle -= 1


# x = 0
# while not num_faro_shuffle == 0:
#     new_list.append(left_side[x])
#     new_list.append(right_side[x])
#     x += 1

cards = input().split()
num_faro_shuffle = int(input())

split_in_half = len(cards) // 2
left_side = cards[0:split_in_half]
right_side = cards[split_in_half:]
new_list = []

while not num_faro_shuffle == 0:
    for i in range(split_in_half):
        new_list.append(left_side[i])
        new_list.append((right_side[i]))
    left_side = new_list[0:split_in_half]
    right_side = new_list[split_in_half:]
    cards = new_list
    new_list = []
    num_faro_shuffle -= 1
print(cards)

