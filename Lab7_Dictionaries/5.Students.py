command = input()
courses = {}

while ":" in command:
    name, id_num, course_name = command.split(":")

    if course_name not in courses:
        courses[course_name] = {}

    courses[course_name][id_num] = name

    command = input()

searched_course = command.lower().split("_")
searched_course_as_str = " ".join(searched_course)

for courses_name in courses:
    if courses_name == searched_course_as_str:
        for each_id, each_student in courses[courses_name].items():
            print(f"{each_student} - {each_id}")

