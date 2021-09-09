x = int(input())
y = int(input())
z = int(input())


def smallest_num(x, y, z):
    list_of_int = [x, y, z]
    result = min(list_of_int)
    return result


print(smallest_num(x, y, z))
