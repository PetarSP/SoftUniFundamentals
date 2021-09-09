employees_happiness = input().split()
factor = int(input())

boosted_employee_happiness = [int(employee) * factor for employee in employees_happiness]
average_happiness = sum(boosted_employee_happiness) // len(boosted_employee_happiness)
greater_than_average_list = [greater for greater in boosted_employee_happiness if greater > average_happiness]
if len(employees_happiness)//2 <= len(greater_than_average_list):
    print(f"Score: {len(greater_than_average_list)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(greater_than_average_list)}/{len(employees_happiness)}. Employees are not happy!")
