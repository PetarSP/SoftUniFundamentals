employee_one = int(input())
employee_two = int(input())
employee_three = int(input())

total_people_count = int(input())

total_people_per_hour = employee_one + employee_two + employee_three
time_needed = 0
while total_people_count > 0:
    time_needed += 1
    total_people_count -= total_people_per_hour

    if time_needed % 4 == 0:
        time_needed += 1


print(f"Time needed: {time_needed}h.")

