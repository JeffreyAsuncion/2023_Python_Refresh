students = ["Hermione", "Harry", "Ron"]

gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# list comprehension
gryffindors = [{"name": student, "house":"Gryffindor"} for student in students]


print(gryffindors)