import sys

list_of_integers = input().split()
n = int(input())
biggest_num = sys.maxsize
biggest_num_index = 0

for loops in range(n):
    for number in list_of_integers:
        number = int(number)
        if number < biggest_num:
            biggest_num = number
    biggest_num_index = list_of_integers.index(f'{biggest_num}')
    list_of_integers.remove(list_of_integers[biggest_num_index])
    biggest_num = sys.maxsize

print(", ".join(list_of_integers))
