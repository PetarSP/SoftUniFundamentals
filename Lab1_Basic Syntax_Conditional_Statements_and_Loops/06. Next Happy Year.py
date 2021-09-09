# year = input()
# new_happy_year = ''
# for i in range(len(year)):
#     if year[0] == year[1] or year[0] == year[2] or year[0] == year[3]:
#         year[0] += 1
#         new_happy_year += year[0]
# print(new_happy_year)

current_year = int(input())

while True:
    current_year += 1
    current_year_as_str = str(current_year)
    if len(set(current_year_as_str)) == len(current_year_as_str):
        print(current_year)
        break