# is_password = True


def password_length(password: str):
    if 6 <= len(password) <= 10:
        return True

    return False


def password_alphanumeric_check(password: str):
    is_alphanum = True

    for i in password:
        if not (i.isalpha() or i.isdigit()):
            is_alphanum = False
            break

    return is_alphanum


def password_2_digits(password: str):
    num_digits = 0
    for i in password:
        if i.isnumeric():
            num_digits += 1
    if num_digits >= 2:
        return True
    else:
        return False


def password_validator(password: str):
    is_password = True
    if not password_length(password):
        is_password = False
        print("Password must be between 6 and 10 characters")
    if not password_alphanumeric_check(password):
        is_password = False
        print("Password must consist only of letters and digits")
    if not password_2_digits(password):
        is_password = False
        print("Password must have at least 2 digits")
    if is_password:
        print("Password is valid")


password = input()
password_validator(password)
