secret_message = input().split()
nums = ''
num_into_ch = ""
final_list = []
letters = []
list_of_words = []
for i in secret_message:
    letters = [j for j in i if j.isalpha()]
    nums = [j for j in i if j.isnumeric()]
    for j in nums:
        num_into_ch += j
    num_into_ch = chr(int(num_into_ch))
    letters[0], letters[-1] = letters[-1], letters[0]
    new_word = num_into_ch + "".join(letters)
    final_list.append(new_word)
    letters = []
    nums = ""
    num_into_ch = ""
print(" ".join(final_list))
