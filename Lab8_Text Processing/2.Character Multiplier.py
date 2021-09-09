first_str, second_str = input().split()

total_sum = 0

first_dict = {first_str: [i for i in first_str]}
second_dict = {second_str: [j for j in second_str]}

diff = len(second_str) - len(first_str)
if diff < 0:
    for each_ch in range(len(second_str)):
        total_sum += (ord(first_str[each_ch]) * ord(second_str[each_ch]))
    for j in range(len(second_str), len(first_str)):
        total_sum += ord(first_str[j])
elif diff > 0:
    for each_ch in range(len(first_str)):
        total_sum +=(ord(second_str[each_ch])* ord(first_str[each_ch]))
    for j in range(len(first_str), len(second_str)):
        total_sum += ord(second_str[j])
else:
    for each_ch in range(len(first_str)):
        total_sum += ord(first_str[each_ch]) * ord(second_str[each_ch])

print(total_sum)


