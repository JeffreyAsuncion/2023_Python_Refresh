# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str and Capitalize user's name
name = name.strip().title()

# Say hello to user
print(f"Hello, {name}")