# Start -> 12:50
import re

text = input()

pattern = r"(\||\#)(?P<item_name>[a-zA-z\s]+)(\1)" \
          r"(?P<expiration_date>\d{2}\/\d{2}\/\d{2})(\1)" \
          r"(?P<calories>[0-9]{1,4}|10000)(\1)"

# Regex Finish -> 13:15
food_list = []
total_calories = 0
matches = re.finditer(pattern, text)

for match in matches:
    object_dict = match.groupdict()
    food_list.append(object_dict)
    total_calories += int(object_dict["calories"])

amount_of_days = total_calories // 2000
print(f"You have food to last you for: {amount_of_days} days!")

for food in food_list:
    print(f"Item: {food['item_name']}, Best before: {food['expiration_date']}, Nutrition: {food['calories']}")






# matches = re.finditer(pattern, text)
# for match in matches:
#     item_name = match.group("item_name")
#     expiration_date = match.group("expiration_date")
#     calories = match.group("calories")
#     food_dict[item_name] = {"exp_date": expiration_date, "cal": int(calories)}
#
# total_calories = 0
# for calories in food_dict.items():
#     total_calories += calories[1]["cal"]
# amount_of_days = total_calories // 2000
# print(f"You have food to last you for: {amount_of_days} days!")
# for food, data in food_dict.items():
#     print(f"Item: {food}, Best before: {data['exp_date']}, Nutrition: {data['cal']}")


# Break - > 13:53 - 14:00
# first attempt judge -> 33/100 -> 14:12


