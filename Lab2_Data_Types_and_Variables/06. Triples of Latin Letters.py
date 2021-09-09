letter_delimiter = int(input())

for i in range(97, 97 + letter_delimiter):
    for k in range(97, 97 + letter_delimiter):
        for j in range(97, 97 + letter_delimiter):
            print(f'{chr(i)}{chr(k)}{chr(j)}')

