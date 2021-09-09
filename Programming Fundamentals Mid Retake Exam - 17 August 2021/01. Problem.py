days_of_the_trip = int(input())
budget = float(input())
group_of_people = int(input())
fuel_price_per_kilometer = float(input())
food_exp_per_person_for_day = float(input())
room_price_per_person_for_night = float(input())

total_food_exp = group_of_people * food_exp_per_person_for_day * days_of_the_trip
total_hotel_room_exp = group_of_people * room_price_per_person_for_night * days_of_the_trip
total_food_hotel_exp = total_food_exp + total_hotel_room_exp
current_consumed_fuel = 0


total_exp = total_food_hotel_exp
if group_of_people > 10:
    total_hotel_room_exp = total_hotel_room_exp - total_hotel_room_exp * 0.25
    total_food_hotel_exp = total_food_exp + total_hotel_room_exp
    total_exp = total_food_hotel_exp
current_day = 1
for day in range(current_day,days_of_the_trip + 1):
    travelled_day_distance = float(input())
    daily_consumed_fuel = travelled_day_distance * fuel_price_per_kilometer
    current_consumed_fuel += daily_consumed_fuel
    total_exp += daily_consumed_fuel

    if current_day % 3 == 0:
        total_exp = total_exp + (total_exp * 0.4)
    if current_day % 5 == 0:
        total_exp = total_exp + (total_exp * 0.4)
    if current_day % 7 == 0:
        total_exp -= (total_exp / group_of_people)
    if total_exp > budget:
        if not (budget - total_exp) == 0:
            print(f"Not enough money to continue the trip. You need {(abs(budget - total_exp)):.2f}$ more.")
            break
    current_day += 1

if budget >= total_exp or (budget - total_exp) == 0:
    print(f"You have reached the destination. You have {(budget - total_exp):.2f}$ budget left.")