num_sheep = int(input())
total_sheep = 0
if num_sheep > 0 and not total_sheep == num_sheep:
    for sheep in range(num_sheep):
        total_sheep += 1
        print(f'{total_sheep} sheep...', end="")


