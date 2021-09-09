
def perfect_num(num):
    for i in range(1, num + 2):
        sum_num = sum(num_list)
        perfect_num = sum_num // 2
        if not num == perfect_num:
            if num % i == 0:
                num_list.append(i)

    if perfect_num == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num = int(input())
num_list = []
perfect_num(num)