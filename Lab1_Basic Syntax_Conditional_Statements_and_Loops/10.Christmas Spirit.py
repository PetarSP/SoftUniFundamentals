quantity = int(input())
days = int(input())

budget = 0
totalSpirit = 0
# prices per peace
OrnamentSet = 2
TreeSkirt = 5
TreeGarlands = 3
TreeLights = 15

total_days = 0
new_quantity = quantity

for each_day in range(1, days + 1):
    while not total_days == each_day:
        if each_day % 11 == 0:
            new_quantity += 2  # increasing quantity in the beginning of every 11th day
        if each_day % 2 == 0:
            budget += new_quantity * OrnamentSet
            totalSpirit += 5
        if each_day % 3 == 0 and each_day % 5 == 0:
            totalSpirit += 30
        if each_day % 3 == 0:  # search for counting every third day!
            budget += (new_quantity * TreeSkirt) + (new_quantity * TreeGarlands)
            totalSpirit += 13
        if each_day % 5 == 0:  # search for counting every fifth day!
            budget += new_quantity * TreeLights
            totalSpirit += 17
        if each_day % 10 == 0:
            totalSpirit -= 20
            budget += TreeLights + TreeGarlands + TreeSkirt

        total_days += 1

if total_days % 10 == 0:
    totalSpirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {totalSpirit}")
