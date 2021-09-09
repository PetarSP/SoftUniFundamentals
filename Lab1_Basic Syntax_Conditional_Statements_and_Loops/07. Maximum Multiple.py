import sys

divisor = int(input())
bound = int(input())

smallest_num = - sys.maxsize
for n in range(bound + 1):
    if n % divisor == 0 and bound >= n > 0:
        if n > smallest_num:
            smallest_num = n
print(smallest_num)

 