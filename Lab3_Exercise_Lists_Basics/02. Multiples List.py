factor = int(input())
count = int(input())

some_list = []
next_num = factor

for num in range(count):
    next_num += factor
    some_list.append(next_num)


print(some_list)