
# calculator
first_num = ""
while not first_num == "end":

    first_num = input("Insert first num:")
    first_num_in_int = int(first_num)
    operation = input("Chose operation:")
    second_num = float(input("Insert second num:"))

    def additional(first_num_in_int, second_num):
        print(first_num_in_int + second_num)


    def multiply(first_num_in_int, second_num):
        print(first_num_in_int * second_num)


    def minus(first_num_in_int, second_num):
        print(first_num_in_int - second_num)


    def divide(first_num_in_int, second_num):
        print(first_num_in_int / second_num)


    if operation == "+":
        additional(first_num_in_int, second_num)
    elif operation == "*":
        multiply(first_num_in_int, second_num)
    elif operation == "-":
        minus(first_num_in_int, second_num)
    elif operation == "/":
        divide(first_num_in_int, second_num)
