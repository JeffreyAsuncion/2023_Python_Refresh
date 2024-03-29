students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(students):
    return students['name']

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")