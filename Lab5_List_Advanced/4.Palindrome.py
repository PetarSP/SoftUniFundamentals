words = input().split()
palindrome = input()


# for el in words:
#     if el[0:] == el[-1:]:
#         print(el)
palindrome_list = [i for i in words if i[::-1] == i[::]]
# palindrome_list = [palindrome_list.append(el) for el in words if el == el.reverse()]
palindrome_count = words.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")
