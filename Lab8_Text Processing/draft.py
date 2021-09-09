for user_name in user_names:
    if not 3 < len(user_name) <= 16:
        is_user_name_valid = False
    if not user_name.isalnum():
        is_user_name_valid = False
        if ("-" or "_") in user_name:
            for i in user_name.split("-"):
                if i.isalnum():
                    is_user_name_valid = True
            for j in user_name.split("_"):
                if j.isalnum():
                    is_user_name_valid = True

new_text = ""
for index in range(len(text)):
    current_symbol = text[index]
    if not current_symbol == ">":
        new_text += current_symbol
    else:
        explosion_strength = text[index + 1]
        new_text += current_symbol
        index += 1