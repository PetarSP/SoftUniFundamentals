import re

pattern = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})\b"
text = input()
valid_num = re.finditer(pattern, text)
matches = [match.group() for match in valid_num]
print(", ".join(matches))