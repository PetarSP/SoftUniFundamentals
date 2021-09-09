
word = input()
sentence = ''
for char in word:
    sentence_power_2 = char * 2
    sentence += sentence_power_2
print(sentence)
