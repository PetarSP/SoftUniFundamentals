list_of_numbers = input().split(", ")

print([list_of_numbers.index(el) for el in list_of_numbers if int(el) % 2 == 0])
