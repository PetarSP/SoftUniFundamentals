# Write a program that receives three whole numbers and print the largest one.

num_1 = int(input("Enter first number."))
num_2 = int(input("Enter second number."))
num_3 = int(input("Enter third number."))

# check which one is the highest num

if num_1 > num_2 and num_1 > num_3:
    print(f"The highest num is the first num = {num_1}")
elif num_2 > num_1 and num_2 > num_3:
    print(f"The highest num is the second num = {num_2}")
else:
    print(f"The highest num is the third num  = {num_3}")
