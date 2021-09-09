import re

furniture = input()
pattern = r">>(?P<Type>[A-Za-z]+)<<(?P<Price>\d+\.?\d+)!(?P<Quantity>\d+)"
furniture_types = []

total_money_spend = 0
while not furniture == "Purchase":
    valid_furniture = re.finditer(pattern, furniture)

    for i in valid_furniture:
        i.groupdict()
        furniture_types.append((i["Type"]))
        total_money_spend += float(i["Price"]) * int(i["Quantity"])

    furniture = input()


print("Bought furniture:")
for i in furniture_types:
    print(i)

print(f"Total money spend: {total_money_spend:.2f}")