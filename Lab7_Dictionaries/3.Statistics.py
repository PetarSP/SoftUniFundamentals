command = input()
# products_list = []
products_dict = {}
while not command == "statistics":
    key, value = command.split(": ")
    if key in products_dict:
        products_dict[key] += int(value)
    else:
        products_dict[key] = int(value)
    # products_list.append(key)
    command = input()

print(f"Products in stock:")

for each_product_name, each_product_value in products_dict.items():
    print(f"- {each_product_name}: {each_product_value}")

print(f"Total Products: {len(products_dict)}\nTotal Quantity: {sum(products_dict.values())}")
