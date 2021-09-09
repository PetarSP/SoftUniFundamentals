# make cozonacs and exchange them for eggs

budget = float(input())
flour_price_1kg = float(input())

# recipe for 1 cozonac = eggs(1pack), flour(1kg), milk(0.250l)

eggs_price_1pack = 0.75 * flour_price_1kg
milk_price_1ltr = flour_price_1kg + 0.25 * flour_price_1kg
milk_price_250ml = milk_price_1ltr / 4

one_cozonac_price = milk_price_250ml + eggs_price_1pack + flour_price_1kg

colored_eggs = 0
cozonacs_num = 0
cozonacs_total_price = 0
possible_cozunacs_num_to_make = int(budget / one_cozonac_price)

while not budget <= one_cozonac_price and not colored_eggs < 0:
    # for every cozonac that you make you receive 3 colored eggs
    # for cozonac in range(0, possible_cozunacs_num_to_make):
    cozonacs_num += 1
    colored_eggs += 3
    cozonacs_total_price += one_cozonac_price
    if cozonacs_num % 3 == 0:
        colored_eggs -= (cozonacs_num - 2)
    budget -= one_cozonac_price

money_left = budget

print(f"You made {cozonacs_num} cozonacs! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
