# collet the necessary inputs: principal, apr, years
# calculate the monthly payment
# show to the user

def calculate_monthly_payment():
    print("This is a monthly payment loan calculator\n\n")
    
    principal = float(input("Enter the loan amount : "))
    apr = float(input("Enter the annual interest rate : "))
    years = int(input("Enter the amount of years : "))
    
    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) **(-amount_of_months))
    
    print(f"The monthly payment for this loan is ${monthly_payment:.2f}")
    
if __name__ == '__main__':
    calculate_monthly_payment()