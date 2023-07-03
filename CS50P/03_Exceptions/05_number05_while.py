while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break 

    
print(f"x is {x}")

# both version work, it is comes down to readability