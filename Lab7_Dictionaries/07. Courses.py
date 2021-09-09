command = input()

courses = {}

while not command == "end":
    course, student = command.split(" : ")
    if course not in courses:
        courses[course] = []
    if not student == "":
        courses[course] += [student]
    command = input()

ordered_courses = sorted(courses.items(), key=lambda x: -len(x[1]))
for course, student in ordered_courses:
    print(f"{course}: {len(courses[course])}")
    for each_student in sorted(student):
        print(f"-- {each_student}")
