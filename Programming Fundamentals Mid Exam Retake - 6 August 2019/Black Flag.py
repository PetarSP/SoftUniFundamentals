days_of_plunder = int(input())

daily_plunder = int(input())
expected_plunder_at_end = float(input())

total_plunder = 0
current_day = 1

while not current_day == days_of_plunder + 1:
    total_plunder += daily_plunder

    if not current_day == 0 and current_day % 3 == 0:
        total_plunder = total_plunder + (daily_plunder * 0.5)
    if not current_day == 0 and current_day % 5 == 0:
        total_plunder = total_plunder - 0.3 * total_plunder
    current_day += 1

if total_plunder >= expected_plunder_at_end:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage_left = 100 - (((expected_plunder_at_end - total_plunder) / expected_plunder_at_end) * 100)
    print(f"Collected only {percentage_left:.2f}% of the plunder.")

