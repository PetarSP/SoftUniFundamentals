delimiter = int(input())

for num in range(1, delimiter + 1):
    num_as_str = str(num)
    result = 0
    for digits in num_as_str:
        digits_as_int = int(digits)
        result += digits_as_int
    if result == 5 or result == 7 or result == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')