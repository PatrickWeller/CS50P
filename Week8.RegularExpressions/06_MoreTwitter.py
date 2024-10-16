# Note - this script doesn't run

# Now let's go back to re.search() where we began to still incorporate some conditional
# element to our code, checking that at least something has been inputted right.
# Or else re.sub() will allow the user to put www.google.com/patrick and it will accept it.
import re

url = input("URL: ").strip()

# So let's use re.search() and try and use brackets to capture the username (.+) at the end
# We're assuming there's nothing after the username
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))

# But the issue here is if I am capturing www\. (or None if I don't type www.)
# So i need to do matches.group(2).
# and let's tighten up with the walrus operator
if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(2))

# But a better solution is not to capture www. by using (?:www\.)
# then I can use matches.group(1) again
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

# Let's make one last change as twitter only accepts certain characters as usernames
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
