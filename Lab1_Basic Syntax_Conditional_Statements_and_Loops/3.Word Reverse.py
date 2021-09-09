#
# def rev():
#     word = input()
#     print((word[::-1]).lower())
#
#
# rev()

# word = input()
#
# rev_word = ""
#
# for i in range(len(word) - 1, -1 , -1):
#     rev_word += word[i]
# print(rev_word)

word = input()

while not word == 'end':
    word_into_list = list(word)
    reversed_list = reversed(word_into_list)
    print(list(reversed_list))
    word = input()

