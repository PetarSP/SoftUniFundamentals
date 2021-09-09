def sum_numbers(x, y):
    result = x + y
    return result


def subtract():
    result = (x + y) - z
    return result


def add_and_subtract(x, y, z):
    return sum_numbers(x,y) - z

x = int(input())
y = int(input())
z = int(input())

print(add_and_subtract(x, y, z))
