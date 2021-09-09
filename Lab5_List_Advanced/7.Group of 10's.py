import math
numbers = list(map(int, input().split(", ")))
group = 0
list_of_numbers = []

find_highest_num = max(numbers)
num_of_possible_groups = math.ceil(find_highest_num / 10)
current_group = 0
next_group = 11

while not num_of_possible_groups == 0:
    for num in numbers:
        if num in range(current_group, next_group):
            list_of_numbers.append(num)
    num_of_possible_groups -= 1
    current_group = next_group
    next_group += 10
    print(f"Group of {current_group - 1}'s: {list_of_numbers}")
    list_of_numbers = []