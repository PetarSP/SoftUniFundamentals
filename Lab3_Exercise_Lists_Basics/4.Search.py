num = int(input())
word = input()

list_of_sentences_one = []
list_of_sentences_two = []

for next_input in range(num):
    sentence = input()
    list_of_sentences_one.append(sentence)
    if word in list_of_sentences_one[len(list_of_sentences_one) - 1]:
        list_of_sentences_two.append(sentence)
print(list_of_sentences_one)
print(list_of_sentences_two)