char_list = input().split(", ")

new_dict = {each_chr: ord(each_chr) for each_chr in char_list}
print(new_dict)
