centuries = int(input())

centuries_years = centuries * 100
centuries_days = int(centuries_years * 365.2422)
centuries_hours = int(centuries_days * 24)
centuries_min = int(centuries_hours * 60)

print(
    f'{centuries} centuries = {centuries_years} years = {centuries_days} days'
    f' = {centuries_hours} hours = {centuries_min} minutes')
