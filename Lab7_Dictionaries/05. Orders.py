
data = input()

products = {}

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = [price, quantity]
    else:
        products[name][1] += int(quantity)
        if not price == products[name][0]:
            products[name][0] = price

    data = input()

for product in products:
    print(f"{product} -> {(products[product][0]*products[product][1]):.2f}")
