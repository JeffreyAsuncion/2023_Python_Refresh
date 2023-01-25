# Next steps 
# export the list to a file or write the class to a file

class ContactInfo:
    def __init__(self, email, user_name, domain, extension):
        self.email = email
        self.user_name = user_name
        self.domain = domain
        self.extension = extension

def welcome():
    print("Welcome to the email slicer\n\n")

def email_slicer():
    
    email = input("Input email to be sliced : ")
    user_name, raw_domain = email.split('@')
    domain, extension = raw_domain.split('.')
    print(f"user_name : {user_name} \ndomain : {domain}\nextension : {extension}")
    contact = ContactInfo(email, user_name, domain, extension)
    contact_list.append(contact)
    return contact_list

def print_contacts():
    print("\n\nList of usernames")
    print("="*20)
    for i in range(len(contact_list)):
        print(contact_list[i].user_name)


if __name__ == '__main__':
    contact_list = []
    num_of_emails = int(input("Enter the number of emails to be sliced (int) : "))
    for i in range(num_of_emails):
        welcome()
        contact_list = email_slicer()
    print_contacts()

