data = input().split(" ")
data_as_str = "".join(data)
empty_dict = {}
# print({each_char: sum(each_char.count(each_char)) for each_char in data_as_str if each_char in data_as_str})

for each_char in data_as_str:
    if each_char not in empty_dict:
        empty_dict[each_char] = {}
        empty_dict[each_char] = 0
    empty_dict[each_char] += 1
for key, value in empty_dict.items():
    print(f"{key} -> {value}")