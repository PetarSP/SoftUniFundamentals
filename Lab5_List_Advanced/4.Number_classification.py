# numbers = input().split(", ")
#
# positive_numbers = [n for n in numbers if int(n) >= 0]
# negative_numbers = [n for n in numbers if int(n) < 0]
# even_numbers = [n for n in numbers if int(n) % 2 == 0]
# odd_numbers = [n for n in numbers if int(n) % 2 == 1]
#
# print(f"Positive: {', '.join(positive_numbers)}\n"
#       f"Negative: {', '.join(negative_numbers)}\n"
#       f"Even: {', '.join(even_numbers)}\n"
#       f"Odd: {', '.join(odd_numbers)}")

numbers = list(map(int, input().split(", ")))  # map invoke func name without calling - without () !!!
nums = list(map(lambda n: int(n), input().split(", ")))  # same as above

