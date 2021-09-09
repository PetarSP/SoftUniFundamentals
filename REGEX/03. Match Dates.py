import re

text = input()

pattern = r"(?P<Day>\d{2})(?P<Separator>[/\.-])(?P<Month>[A-Z][a-z]{2})(?P=Separator)(?P<Year>\d{4})"

valid_dates = re.finditer(pattern, text)
for dates in valid_dates:
    current_date = dates.groupdict()
    print(f"Day: {current_date['Day']}, Month: {current_date['Month']}"
          f", Year: {current_date['Year']}")
