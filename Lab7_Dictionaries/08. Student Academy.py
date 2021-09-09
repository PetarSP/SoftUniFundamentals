def mean(some_list: list):
    avg = sum(some_list) / len(some_list)
    return avg


pair_of_rows = int(input())

classmate = {}
special_class = {}

for index in range(0, pair_of_rows * 2, 2):
    student_name = input()
    grade = float(input())

    if student_name not in classmate:
        classmate[student_name] = []
    classmate[student_name] += [grade]

for special_students, grades in classmate.items():
    if mean(classmate[special_students]) >= 4.50:
        special_class[special_students] = mean(grades)

for students, grades in sorted(special_class.items(), key=lambda x: -x[1]):
    print(f"{students} -> {grades:.2f}")
