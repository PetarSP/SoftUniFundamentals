some_str = input()

digits = ""
letters = ""
symbols = ""

for each_chr in some_str:
    if each_chr.isdigit():
        digits += each_chr
    elif each_chr.isalpha():
        letters += each_chr
    else:
        symbols += each_chr

print(f"{digits}\n"
      f"{letters}\n"
      f"{symbols}")
