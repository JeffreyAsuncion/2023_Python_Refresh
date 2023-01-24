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
        a = int(input("Input first number : "))
        b = int(input("Input second number : "))
        sub(a, b)
    elif choice.lower() == "c":
        print("Multiplication")
        a = int(input("Input first number : "))
        b = int(input("Input second number : "))
        mul(a, b)
    elif choice.lower() == "d":
        print("Division")
        a = int(input("Input first number : "))
        b = int(input("Input second number : "))
        div(a, b)
    elif choice.lower() == 'e':
        print("\nGoodbye...\n")
        break
