user_names = input().split(", ")
valid_char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"
is_user_name_valid = False
valid_user_names = []

for word in user_names:
    for char in word:
        if char in valid_char:
            is_user_name_valid = True
        else:
            is_user_name_valid = False
            break
    if not 3 < len(word) <= 16:
        is_user_name_valid = False
    if is_user_name_valid:
        valid_user_names.append(word)

print("\n".join(valid_user_names))
