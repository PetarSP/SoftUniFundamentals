numbers_in_str = input()

numbers_in_list = numbers_in_str.split(" ")

flipped_list_of_num = []

for num in numbers_in_list:
    num_in_int = int(num)
    num_in_int *= -1
    flipped_list_of_num.append(num_in_int)

print(flipped_list_of_num)
