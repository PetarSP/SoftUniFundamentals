text = input()

print("".join([str(ch) for ch in text if ch not in "aouei"]).lower())

