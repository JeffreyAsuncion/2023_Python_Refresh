import re

url = input("URL: ").strip()

#twitter requirements for username
# a-z 0-9 or _
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/[a-z0-9_]+$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1)) 