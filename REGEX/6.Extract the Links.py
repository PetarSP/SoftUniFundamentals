import re

text = input()
pattern = r"(?P<Email>(?P<Sub_Domain>www)\.(?P<Domain_name>[A-Za-z0-9\-]+)" \
          r"(?P<Domain_extension>(?P<Domain_block>(\.[a-z]+)+)))"

while not text == "":
    matches = re.finditer(pattern, text)
    for match in matches:
        print(match.group("Email"))

    text = input()
