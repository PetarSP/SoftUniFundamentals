def letters_in_between(a: str, b: str):
    a_into_num = ord(a)
    b_into_num = ord(b)
    for i in range(a_into_num + 1, b_into_num):
        print(chr(i), end=" ")


char_one = input()
char_two = input()
letters_in_between(char_one, char_two)
