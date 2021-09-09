command = input()

companies = {}

while not command == "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in companies:
        companies[company_name] = []
    if employee_id not in companies[company_name]:
        companies[company_name] += [employee_id]

    command = input()

ordered_companies = sorted(companies.items(), key=lambda x: x[0])
for company_name, employee_id in ordered_companies:
    print(f"{company_name}")
    for each_client in employee_id:
        print(f"-- {each_client}")


