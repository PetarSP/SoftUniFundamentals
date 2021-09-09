# def sum_of_even_odd(num: int):
#     even_sum = 0
#     odd_sum = 0
#     i_to_int = [int(i) for i in num]
#     for i in i_to_int:
#         if i % 2 == 0:
#             even_sum += i
#         else:
#             odd_sum += i
#     return print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
#
# num = input()
#
# sum_of_even_odd(num)


# advanced technics

def even_odd_sum(num: str):
    even = [int(x) for x in number if int(x) % 2 == 0]
    odd = [int(x) for x in number if not int(x) % 2 == 0]
    return f"Odd sum = {sum(odd)}, Even sum = {sum(even)}"


number = input()

print(even_odd_sum(number))











