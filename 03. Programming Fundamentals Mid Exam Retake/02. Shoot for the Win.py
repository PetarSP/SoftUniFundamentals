# 14:20

targets = input().split()

int_targets = [int(target) for target in targets]

count_of_shot_targets = 0

command = input()

while not command == "End":
    index = int(command)

    if index < len(int_targets):
        current_target = int_targets[index]
        int_targets[index] = -1
        count_of_shot_targets += 1
        for each_target_index in range(len(int_targets)):
            if not int_targets[each_target_index] == -1:
                if int_targets[each_target_index] > current_target:
                    int_targets[each_target_index] -= current_target

                elif int_targets[each_target_index] <= current_target:
                    int_targets[each_target_index] += current_target

    current_target = 0
    command = input()
str_targets = [str(target) for target in int_targets]
print(f"Shot targets: {count_of_shot_targets} -> {' '.join(str_targets)}")

# 14:55