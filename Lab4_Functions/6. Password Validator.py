# def password_validator(password):
#     is_valid = True
#     if len(password) in range(6, 11):
#         is_valid = True
#     else:
#         is_valid = False
#         print("Password must be between 6 and 10 characters")
#
#     for i in password:
#         if ord(i) in range(48, 58) or ord(i) in range(65, 91) or ord(i) in range(97, 123):
#             is_valid = True
#         else:
#             is_valid = False
#             print("Password must consist only of letters and digits")
#             break
#
#     for j in password:
#         if ord(j) in range(48, 58):
#             sum_digits = 0
#             sum_digits += 1
#     if sum_digits >= 2:
#         is_valid = True
#     else:
#         is_valid = False
#         print("Password must have at least 2 digits")
#
#     if is_valid:
#         print("Password is valid")
#
#
# password = input()
#
# password_validator(password)
