given_number = int(input())

positive_num = []
negative_num = []

for num_lines in range(given_number):
    num = int(input())
    if num >= 0:
        positive_num.append(num)
    else:
        negative_num.append((num))

sum_negatives = 0

for i in negative_num:
    sum_negatives += i

print(positive_num)
print(negative_num)

print(f"Count of positives: {len(positive_num)}. Sum of negatives: {sum_negatives}")