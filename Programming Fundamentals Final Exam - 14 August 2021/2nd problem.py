import re

number_of_inputs = int(input())
pattern = r"(?P<surr>[\W\w]+)>(?P<first_group>\d{3})\|(?P<second_group>[a-z]{3})\|(?P<third_group>[A-Z]{3})\|(?P<fourth_group>[^<>]{3})<(?P=surr)"
valid_passwords = []
for _ in range(number_of_inputs):
    password = input()
    matches = re.finditer(pattern, password)
    some_list = [match.groupdict() for match in matches if match]
    valid_passwords.append(some_list)
    if valid_passwords == [[]]:
        valid_passwords = []
        print("Try another password!")
    else:
        for i in valid_passwords:
            first_group = i[0]["first_group"]
            second_group = i[0]["second_group"]
            third_group = i[0]["third_group"]
            fourth_group = i[0]["fourth_group"]
            print(f"Password: {first_group+second_group+third_group+fourth_group}")
        valid_passwords= []





