import re

url = input("URL: ").strip()

# this works if they enter twitter but if they enter google.com?
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")