def main():
    # this is a tuple
    student = get_student()
    # TypeError: 'tuple' object does not support item assignment
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) # tuple


if __name__ == "__main__":
    main()
