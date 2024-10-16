########### Seasons of Love ###########

# Assuming there are 365 days in a year, there are 525600 minutes in that same year.
# But how many minutes are in more years, and what about leap years with an extra 1,440 minutes.
# Let's use the datatime library that has a class called date.
# docs.python.org/3/library/datetime.html#date-objects

# implement a program that prompts the user for their date of birth in YYYY-MM-DD format
# and then sings prints how old they are in minutes, rounded to the nearest integer,
# using English words instead of numerals, just like the song from Rent, without any and between words.
# Since a user might not know the time at which they were born, assume, for simplicity,
# that the user was born at midnight (i.e., 00:00:00) on that date.
# And assume that the current time is also midnight.
# In other words, even if the user runs the program at noon,
# assume that it’s actually midnight, on the same date.
# Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

# Feel free to install other programs listed in the hinted.

# Exit via sys.exit if the user does not input a date in YYYY-MM-DD format.
# Ensure that your program will not raise any exceptions.

# Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py,
# one or more functions that test your implementation of any functions besides main in seasons.py thoroughly,
# each of whose names should begin with test_

from datetime import date, timedelta
import sys
import inflect

def main():
    dob = get_dob()
    today = date.today()
    time_diff = today - dob
    minutes = convert_to_minutes(time_diff)
    p = inflect.engine()
    words = p.number_to_words(minutes, wantlist=True, andword="")
    sentence = insert_commas(words)
    print(f"{sentence.capitalize()} minutes")



def get_dob():
    dob = input("Date of Birth: ")
    try:
        return date.fromisoformat(dob)
    except:
        sys.exit("Invalid date")


def convert_to_minutes(time_diff):
    minutes = time_diff / timedelta(minutes=1)
    return int(minutes)

def insert_commas(words):
    sentence = ""
    for word in words:
        if sentence:
            sentence += (f", {word}")
        else:
            sentence = word
    return sentence

if __name__ == "__main__":
    main()
