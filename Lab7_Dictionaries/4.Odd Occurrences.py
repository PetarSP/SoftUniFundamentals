data = input().lower().split()
data_dict = {}
new_list = []
for each_el in data:
    if each_el not in data_dict:
        data_dict[each_el] = 0
    else:
        data_dict[each_el] += 1

for element in data_dict:
    if data_dict.get(element) % 2 == 0:
        new_list.append(element)
print(" ".join(new_list))
