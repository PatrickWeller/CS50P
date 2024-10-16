# Working 9 to 5

# Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock.
# Accordingly, instead of “09:00 to 17:00”,
# many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”),

# In a file called working.py,
# implement a function called convert that expects a str
# in any of the 12-hour formats below and
# returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
# Expect that AM and PM will be capitalized (with no periods therein)
# and that there will be a space before each.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM

# Raise a ValueError instead if the input to convert is not in either of those formats
# or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
# But do not assume that someone’s hours will start ante meridiem and end post meridiem;
# someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

# Either before or after you implement convert in working.py,
# additionally implement, in a file called test_working.py,
# three or more functions that collectively test your implementation of convert thoroughly,
# each of whose names should begin with test_ so that you can execute your tests with:
# pytest test_working.py

import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if match := re.search(r"^(.*) ([AP]M) to (.*) ([AP]M)$", s):
        times = match.group(1, 3)
        meridiems = match.group(2, 4)
        data = {}

        for time, meridiem, i in zip(times, meridiems, range(1, 3)):
            if time_splits := re.search(r"(\d\d?):?(\d\d)?", time):
                hour = time_splits.group(1)
                minutes = time_splits.group(2)
            else:
                raise ValueError

            # Check for hours > 12
            if int(hour) > 12:
                raise ValueError

            if minutes == None:
                minutes = "00"
            elif int(minutes) > 59:
                raise ValueError
            else:
                pass

            if int(hour) == 12 and meridiem == "PM":
                pass
            elif int(hour) != 12 and meridiem == "PM":
                hour = str(int(hour) + 12)
            elif int(hour) == 12 and meridiem == "AM":
                hour = "00"
            elif int(hour) < 10:
                hour = ("0" + hour)
            else:
                pass

            (data[f'hour{i}']) = hour
            (data[f'minutes{i}']) = minutes

        return data["hour1"] + ":" + data["minutes1"] + " to " + data["hour2"] + ":" + data["minutes2"]
    else:
        raise ValueError


if __name__ == "__main__":
    main()
