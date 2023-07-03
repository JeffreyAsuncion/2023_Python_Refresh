try:
    x = int(input("What's x? "))
   
except ValueError:
    print("x is not an integer") 

# moved this to clean up the try  
print(f"x is {x}")

# this breaks if not a number