text = input()

new_text = ""
bomb_power = 0
i = 0

while i < len(text):
    current_symbol = text[i]

    if current_symbol == ">":
        bomb_power += int(text[i + 1])
        new_text += ">"
    else:
        if bomb_power > 0:
            bomb_power -= 1
        else:
            new_text += current_symbol
    i += 1
print(new_text)