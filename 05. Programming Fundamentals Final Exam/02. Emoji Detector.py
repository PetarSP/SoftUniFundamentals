import re

text = input()
emoji_cool = 0
pattern_one = r"(?P<start_end>\:\:|\*\*)([A-Z][a-z]{2,})(?P=start_end)"
pattern_two = r"\d"

matches_emoji = re.finditer(pattern_one, text)
matches_nums = re.finditer(pattern_two, text)
cool_threshold = 1

cool_emojis = [match_emoji.group() for match_emoji in matches_emoji]

for match_nums in matches_nums:
    for each_num in match_nums.group():
        cool_threshold *= int(each_num)

print(f"Cool threshold: {cool_threshold}\n{len(cool_emojis)} emojis found in the text. The cool ones are:")

for each_emoji in cool_emojis:
    for letter in each_emoji:
        if letter.isalnum():
            emoji_cool += ord(letter)
    if emoji_cool >= cool_threshold:
        print(f"{each_emoji}")
        emoji_cool = 0

