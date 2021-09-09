number_of_inputs = int(input())

even = []
odd = []
negative = []
positive = []

for _ in range(number_of_inputs):
    num = int(input())
    if num < 0:
        negative.append(num)
    if num % 2 == 0:
        even.append(num)
    if num % 2 == 1:
        odd.append(num)
    if num >= 0:
        positive.append(num)

command = input()

if command == 'even':
    print(even)
elif command == 'odd':
    print(odd)
elif command == 'negative':
    print(negative)
elif command == 'positive':
    print(positive)
