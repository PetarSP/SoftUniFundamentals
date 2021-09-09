total_num_water_ingress = int(input())
total_water = 0

for each_water_ingr in range(total_num_water_ingress):
    each_water_ingr = int(input())
    total_water += each_water_ingr
    if total_water > 255:
        total_water -= each_water_ingr
        print('Insufficient capacity!')
        continue
print(total_water)
