# Write a program that reads a floating-point number and prints "zero" if the number is zero. Otherwise, it should print
# "positive" or "negative". The program should add "small" if the absolute value of the number is less than 1, or "large"
# if it exceeds 1 000 000.

num = float(input())

if num == 0:
    print('zero')

elif num > 0:
    if num < 1:
        print('small positive')
    elif num > 1000000:
        print('large positive')
    else:
        print('positive')

else:
    if abs(num) < 1:
        print('small negative')
    elif abs(num) > 1000000:
        print('large negative')
    else:
        print('negative')


