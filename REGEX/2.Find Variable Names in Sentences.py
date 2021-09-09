import re

text = input()

pattern = r"\b_(?P<var>[A-Za-z0-9]+)\b"

valid_var = re.finditer(pattern, text)
final_list = [i.group("var") for i in valid_var]

print(",".join(final_list))