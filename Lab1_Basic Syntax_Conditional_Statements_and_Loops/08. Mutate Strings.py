# bubble gym
# turttle hum

first_str = input()
second_str = input()
last_str = first_str

for symbol in range(len(first_str)):
    left_part = second_str[:symbol + 1]
    right_part = first_str[symbol + 1:]
    current_str = left_part + right_part
    if current_str == last_str:
        continue
    print(current_str)
    last_str = current_str
