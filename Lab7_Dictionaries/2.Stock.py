products = input().split()
products_dict = {}


for index in range(0, len(products), 2):
    key = products[index]
    value = products[index + 1]
    products_dict[key] = value
products_to_check = input().split()

for each_product in products_to_check:
    if each_product in products_dict:
        print(f"We have {products_dict[each_product]} of {each_product} left")
    else:
        print(f"Sorry, we don't have {each_product}")

