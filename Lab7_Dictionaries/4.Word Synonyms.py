n = int(input())  # total number of words
all_words = [input() for word in range(0, 2 * n)]  # list of words
synonym_dict = {}

for word_index in range(0, len(all_words), 2):
    if all_words[word_index] not in synonym_dict:
        synonym_dict[all_words[word_index]] = [all_words[word_index + 1]]
    else:
        synonym_dict[all_words[word_index]] += [all_words[word_index + 1]]

for key, value in synonym_dict.items():
    print(f"{key} - {', '.join(value)}")

