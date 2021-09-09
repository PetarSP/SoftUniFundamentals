str_to_rmv = input()
word = input()

while str_to_rmv in word:
    word = word.replace(str_to_rmv, "")

print(word)