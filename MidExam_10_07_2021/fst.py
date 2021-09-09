import math

budget = float(input())
num_students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

total_flour_price = flour_price * num_students
total_egg_price = 10 * egg_price * num_students
total_apron_price = apron_price * math.ceil(num_students +0.2*num_students)

# educational_set = flour_price * 1 + egg_price * 10 + math.ceil(apron_price * 1 + (num_students + num_students*0.20))
total_spend = (total_flour_price + total_egg_price + total_apron_price)
package_for_each_student = total_spend / num_students
total = 0
for each_student in range (1, num_students +1 ):
    if each_student % 5 == 0:
        total_spend -= flour_price


if total_spend <= budget:
    print(f"Items purchased for {total_spend:.2f}$.")
elif total_spend > budget:
    print(f"{(total_spend - budget):.2f}$ more needed.")
