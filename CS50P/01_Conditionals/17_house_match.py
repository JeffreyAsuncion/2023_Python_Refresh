name = input("What's your name? ")

# match is in Python 3.10 and higher
match name: 
    case "Harry":
        print("Gryffindor")
    case "Herminone":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case  "Draco":
        print("Slytherin")
    case _:
        print("Who?")