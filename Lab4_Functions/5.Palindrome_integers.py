def palindrome_int():
    palindrome_list = ["True" if el == el[::-1] else "False" for el in check_list]
    joined = "\n".join(palindrome_list)
    return print(joined)

check_list = input().split(", ")

palindrome_int()

