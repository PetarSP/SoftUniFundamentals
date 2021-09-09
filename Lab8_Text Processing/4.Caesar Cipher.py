text = input()

# encrypted_text = ""
# for el in reg_text:
#     new_el = chr(ord(el) + 3)
#     encrypted_text += new_el
#
# print(encrypted_text)

encrypted_text = "".join([(chr(ord(el) + 3)) for el in text])
print(encrypted_text)