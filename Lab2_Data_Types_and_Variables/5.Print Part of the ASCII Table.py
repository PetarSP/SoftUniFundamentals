start = int(input())
end = int(input())

for ascii_symbol in range(start, end + 1):
    print(chr(ascii_symbol), end=' ')
