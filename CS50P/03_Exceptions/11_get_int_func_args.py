def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) # makes this more  dynamic
            
        except ValueError:
            pass
    

main()
