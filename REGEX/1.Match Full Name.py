import re

text = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
valid_names = re.search(pattern, text)
print(valid_names)
