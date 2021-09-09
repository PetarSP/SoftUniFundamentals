def free_chairs(num_of_visitors: int, num_of_chairs: str):
    number_of_room = current_room
    num_of_chairs = int(len(num_of_chairs))

    if num_of_visitors > num_of_chairs:
        needed_chairs_in_room = num_of_visitors - num_of_chairs
        print(f"{needed_chairs_in_room} more chairs needed in room {number_of_room}")



num_of_rooms = int(input())
current_room = 0
total_num_chairs = 0
total_num_visitors = 0
while not num_of_rooms == 0:
    num_of_chairs_and_visitors = input().split()
    num_of_chairs = num_of_chairs_and_visitors[0]
    num_of_visitors = int(num_of_chairs_and_visitors[1])

    num_of_rooms -= 1
    current_room += 1
    total_num_chairs += len(num_of_chairs)
    total_num_visitors += num_of_visitors

    free_chairs(num_of_visitors, num_of_chairs)
if total_num_chairs >= total_num_visitors:
    total_free_chairs = total_num_chairs - total_num_visitors
    print(f"Game On, {total_free_chairs} free chairs left")
