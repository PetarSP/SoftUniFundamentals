import re

text = input().lower()
given_word = input().lower()

pattern = rf"\b{given_word}\b"
all_valid_words = re.finditer(pattern,text)
all_valid_words = [valid_word.group() for valid_word in all_valid_words]
print(len(all_valid_words))