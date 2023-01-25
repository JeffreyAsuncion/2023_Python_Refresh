# define the functions needed : add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")

def sub(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}")

def mul(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}")

def div(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer}")

def get_input():
    a = int(input("Input first number : "))
    b = int(input("Input second number : "))
    return a,b 

while True:
    print("\nWelcome to the Basic Calculator")
    print("="*20)    
    print("A.   Addition")
    print("B.   Subtraction")
    print("C.   Multiplication")
    print("D.   Division")
    print("E.   EXIT!!!")

    choice = input("Enter your choice : ")
    if choice.lower() == "a":
        print("Addition")
        a,b = get_input()
        add(a, b)
    elif choice.lower() == "b":
        print("Subtraction")
        a,b = get_input()
        sub(a, b)
    elif choice.lower() == "c":
        print("Multiplication")
        a,b = get_input()
        mul(a, b)
    elif choice.lower() == "d":
        print("Division")
        a,b = get_input()
        div(a, b)
    elif choice.lower() == 'e':
        print("\nGoodbye...\n")
        break
