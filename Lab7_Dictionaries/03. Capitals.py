country_names = input().split(", ")
capital_cities = input().split(", ")

country_capital_dict = dict(zip(country_names, capital_cities))

for each_country, each_capital in country_capital_dict.items():
    print(f"{each_country} -> {each_capital}")