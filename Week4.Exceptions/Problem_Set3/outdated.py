# outdated.py

# In the United States,
# dates are typically formatted in month-day-year order (MM/DD/YYYY),
# otherwise known as middle-endian order,
# which is arguably bad design.

# Dates in that format can’t be easily sorted
# because the date’s year comes last instead of first.
# Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program
# (e.g., a spreadsheet).

# Dates in that format are also ambiguous.
# Harvard was founded on September 8, 1636,
# but 9/8/1636 could also be interpreted as August 9, 1636!

# Fortunately, computers tend to use ISO 8601,
# an international standard that prescribes that dates
# should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country,
# formatting years with four digits, months with two digits, and days with two digits,
# “padding” each with leading zeroes as needed.

# In a file called outdated.py,
# implement a program that prompts the user for a date, anno Domini,
# in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
# wherein the month in the latter might be any of the values in the list below:

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Then output that same date in YYYY-MM-DD format.
# If the user’s input is not a valid date in either format,
# prompt the user again.

# Assume that every month has no more than 31 days;
# no need to validate whether a month has 28, 29, 30, or 31 days.

def main():
    while True:
        user_date = input("Date: ").strip()
        if check1(user_date) == True:
            print(convert1(user_date))
            break
        elif check2(user_date) == True:
            print(convert2(user_date))
            break
        else:
            pass


# Check if format M/D/YYYY
def check1(x):
    separated = x.split('/', maxsplit=2)

    if (separated[0].isdigit() and
        0 < len(separated[0]) < 3 and
        0 < (int(separated[0])) < 13 and
        separated[1].isdigit() and
        0 < len(separated[1]) < 3 and
        0 < (int(separated[1])) < 31 and
        separated[2].isdigit() and
        len(separated[2]) == 4):
        return True
    else:
        return False

# Convert M/D/YYYY to YYYY-MM-DD
def convert1(x):
    date_split = x.split('/', maxsplit=2)
    return(date_split[2] + "-" + f"{int(date_split[0]):02}" + "-" + f"{int(date_split[1]):02}")

# Check if format 'month day, year'
def check2(x):
    if "," not in x:
        return False
    date_temp = x.split(", ")
    date_temp = [unit.split() for unit in date_temp]
    date_split = [word for sublist in date_temp for word in sublist]
    if (date_split[0] in months and
        date_split[1].isdigit() and
        0 < len(date_split[1]) < 3 and
        0 < int(date_split[1]) < 32 and
        date_split[2].isdigit() and
        len(date_split[2]) == 4):
        return True
    else:
        return False

# convert 'month day, year' to YYYY-MM-DD
def convert2(x):
    date_temp = x.split(", ")
    date_temp = [unit.split() for unit in date_temp]
    date_split = [word for sublist in date_temp for word in sublist]
    return(date_split[2] + "-" + f"{(months.index(date_split[0]) + 1):02}" + "-" + f"{int(date_split[1]):02}")


main()
