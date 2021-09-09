import re

text = input()
pattern_one = r"\w"
updated_test = []
while re.findall(pattern_one, text):
    pattern_two = r"\d+"
    nums = re.findall(pattern_two, text)
    updated_test += nums
    text = input()

print(" ".join(updated_test))