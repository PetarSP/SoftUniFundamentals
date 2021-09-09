# 10:20

number_of_cars = int(input())
car_dict = {}

for cars in range(number_of_cars):
    car_input = input()
    car, mileage, fuel = car_input.split("|")
    car_dict[car] = {}
    car_dict[car]["mileage"] = int(mileage)
    car_dict[car]["fuel"] = int(fuel)

command = input()
while not command == "Stop":
    command = command.split(" : ")
    instruction = command[0]
    car = command[1]
    if instruction == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if car_dict[car]["fuel"] <= fuel:
            print(f"Not enough fuel to make that ride")
        else:
            car_dict[car]["mileage"] += distance
            car_dict[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_dict[car]["mileage"] > 100000:
                print(f"Time to sell the {car}!")
                del car_dict[car]

    elif instruction == "Refuel":
        fuel = int(command[2])
        if car_dict[car]["fuel"] + fuel > 75:
            fuel_needed = 75 - car_dict[car]["fuel"]
            car_dict[car]["fuel"] += fuel_needed
            print(f"{car} refueled with {fuel_needed} liters")
        else:
            car_dict[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif instruction == "Revert":
        kilometers = int(command[2])
        car_dict[car]["mileage"] -= kilometers
        if car_dict[car]["mileage"] < 10000:
            car_dict[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

sorted_car_dict = sorted(car_dict.items(), key=lambda x: (-x[1]["mileage"], x[0]))
for car in sorted_car_dict:
    print(f"{car[0]} -> Mileage: {car[1]['mileage']} kms, Fuel in the tank: {car[1]['fuel']} lt.")
