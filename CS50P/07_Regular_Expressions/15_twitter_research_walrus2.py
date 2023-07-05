import re

url = input("URL: ").strip()

# tighten it up, clean, and more pythonic
# the (?:...) is optional and not considered group 1. like ? ternary operator
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1)) # this is back to group(1)