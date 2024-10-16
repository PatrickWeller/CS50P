import re

locations = {"+1": "United States", "+62": "Indonesia", "+44": "United Kingdom" }

def main():
    pattern = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group(1)
        print(locations[country_code])
    else:
        print("Invalid")

main()

# I've used indices to get capture group 1
# but what if there are many capture groups?
# We can give them a name like so.
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
# Then later make use of country code, recalling it not with indices
if match:
        country_code = match.group("country_code")
        print(locations[country_code])
    else:
        print("Invalid")
