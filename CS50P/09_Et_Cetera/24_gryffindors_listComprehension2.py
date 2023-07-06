students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"
       
# using filter
gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=is_gryffindor):
#     print(gryffindor["name"],1)

# using lambda function
for gryffindor in sorted(gryffindors, key=lambda s:s["name"]):
    print(gryffindor["name"],2)