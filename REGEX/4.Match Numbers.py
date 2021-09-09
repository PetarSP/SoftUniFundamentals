# find all integers and floating point numbers in a str

import re

text = input()

pattern = r"(^|(?<=\s))(-?\d+(\.\d+)?)($|(?=\s))"
valid_nums = re.finditer(pattern, text)

list_valid_nums = [num.group() for num in valid_nums]
print(*list_valid_nums)