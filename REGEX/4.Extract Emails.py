import re

# email format: "{user}@{host}"
emails = input()

pattern = rf"(?P<Email>(?P<User>(?<=\s)[A-Za-z0-9]+[\.\-\_]*[A-Za-z0-9]+)\@(?P<Domain>(([A-Za-z\-?]+)[A-Za-z]+(\.[A-Za-z]+)+)))"

valid_emails = re.finditer(pattern,emails)
valid_emails = [valid_mail.group() for valid_mail in valid_emails]
print("\n".join(valid_emails))