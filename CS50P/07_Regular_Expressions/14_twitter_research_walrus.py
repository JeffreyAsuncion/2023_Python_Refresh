import re

url = input("URL: ").strip()

# tighten it up, clean, and more pythonic
if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(2)) # due to the optional www group