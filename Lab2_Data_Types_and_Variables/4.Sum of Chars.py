number_of_the_lines = int(input())

total_sum = 0
for letter in range(0, number_of_the_lines):
    letter = input()
    for ascii_letter in letter:
        letter_ascii = ord(letter)
        total_sum += letter_ascii


print(f"The sum equals: {total_sum}")

