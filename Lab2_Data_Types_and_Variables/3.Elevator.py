import math

number_of_people = int(input())
capacity_of_elevator = int(input())

num_full_courses = math.ceil(number_of_people / capacity_of_elevator)
# num_of_additional_people = (number_of_people - (num_full_courses * capacity_of_elevator))
# num_of_additional_courses = math.ceil(num_of_additional_people / capacity_of_elevator) - num_full_courses

# if num_full_courses == 1:
#     print('All the persons fit inside the elevator. Only one course_name is needed.')
# else:
#     print(f'{num_full_courses} courses * {capacity_of_elevator} + {num_of_additional_courses} * {num_of_additional_people}')

print(num_full_courses)
