# ask the user if they want to generate a password
# if yes, ask for password length
    # generate password
    # pring password
# otherwise response is no, exit program  


import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    
    password_length = int(input("How long would you like your password to be? : "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    password = "".join(password)
    print(password)
   
   
if __name__ == "__main__":
    option = input("Do you want to generate a password? (Yes/No) : ")
    
    if option.lower() == "yes":
        generate_password()
    elif option.lower() == "no":
        print("Goodbye!")
        quit()
    else:
        print("Invalid input! Please try agagin...")
        quit()