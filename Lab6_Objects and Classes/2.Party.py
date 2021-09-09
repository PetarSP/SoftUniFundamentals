class Party:
    def __init__(self):
        self.people = []


command = input()
my_party = Party()
while not command == "End":
    my_party.people.append(command)
    command = input()

print(f"Going: {', '.join(my_party.people)}")
print(f"Total: {len(my_party.people)}")
