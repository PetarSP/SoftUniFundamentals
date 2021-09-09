text = input()

new_text = ""
for index in range(len(text)):
    current_letter = text[index]
    if (index + 1) < len(text):
        next_letter = text[index + 1]
        if not current_letter == next_letter:
            new_text += current_letter
    elif index == len(text) - 1:
        new_text += current_letter
        break


print(new_text)
