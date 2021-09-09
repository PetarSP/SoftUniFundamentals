first_list_of_str = input().split(", ")
second_list_of_str = input().split(", ")
final_list = []
# noinspection PyTypeChecker

for i in first_list_of_str:
    for j in second_list_of_str:
        if i in j:
            final_list.append(i)
            break

print(final_list)
