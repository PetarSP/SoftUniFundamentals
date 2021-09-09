first_str = input()
sec_str = input()
third_str = input()

rearranged = [third_str, sec_str, first_str]
rearranged[0], rearranged[2] = rearranged[2], rearranged[0]
print(rearranged)
