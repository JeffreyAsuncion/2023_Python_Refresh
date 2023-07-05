class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        # return f"{self.name} from {self.house}"
        return f"{self.name} from {self.house}"
    
    def charm(self):
        # match is for python 3.10
        if self.patronus == "Stag":
            return "🐎"
        elif self.patronus == "Otter":
            return "🐠"
        elif self.patronus == "Jack Russell terrier":
            return "🐶"
        else:
            return "🪄"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)
    

if __name__ == "__main__":
    main()
