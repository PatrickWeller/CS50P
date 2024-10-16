# Now I can't madke all the data for this
# But I've made a small file called views.csv
# It has three columns,
# id,engligh_title,fake_title
# It relates to prints of Mount Fuji made by an artist

# But you see I don't have the jpg files that relate to these
# So I can never actually execute the code I will write
# But the jpgs would all be related to the id column of the file
# e.g. the jpgs would be called 1.jpg, 2.jpg, 3.jpg

# Our goal is to read into the views.csv file,
# then do image analysis on the images. Such as how bright they are.
# 1 is brightest white, 0 is black.
import csv
import numpy as np
from PIL import Image

def main():
    # I'm going to open two files at one time, once for reading, once for writing
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        # Remember Dict Reader reads each line as a dictionary
        reader = csv.DictReader(views)
        # Can write dictionaries to a file, each as a new line
        # analysis should have the same field names as the views file being read
        # But we also want to add the brightness column
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            # Calculate brightness for each row image
            brightness = calculate_brightness(f"{row['id']}.jpg")
            # Write to analysis.csv new rows, copying the rows from our open views file
            # But then adding brightness as the fourth value in each row
            writer.writerow(
                {
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "fake_title": row["fake_title"],
                    "brightness": round(brightness, 2)
                }
            )


### Or can save time like below, just adding brightness to the read row
# Then writing that row
# for row in reader:
#   row["brightness"] = round(calculate_brightness(f"{row['id']}.jpg"), 2)
#   write.writerow(row)

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()

