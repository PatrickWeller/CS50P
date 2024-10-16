# shirt.py   CS50 P-Shirt

# After finishing CS50 itself,
# students on campus at Harvard traditionally receive their very own I took CS50 t-shirt.
# No need to buy one online, but like to try one on virtually?

# In a file called shirt.py,
# implement a program that expects exactly two command-line arguments:

# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
# The program should then overlay shirt.png (which has a transparent background)
# on the input after resizing and cropping the input to be the same size,
# saving the result as its output.

# Open the input with Image.open,
# per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
# resize and crop the input with ImageOps.fit,
# per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
# using default values for method, bleed, and centering,
# overlay the shirt with Image.paste,
# per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste,
# and save the result with Image.save,
# per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

# The program should instead exit via sys.exit:

# if the user does not specify exactly two command-line arguments,
# if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
# if the input’s name does not have the same extension as the output’s name, or
# if the specified input does not exist.

# Assume that the input will be a photo of someone posing in just the right way,
# like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.
import sys
from PIL import Image
from PIL import ImageOps
import os

def main():
    check_arg_num()
    input = sys.argv[1]
    output = sys.argv[2]
    check_image_input(input, output)
    wear_tshirt(input, output)

def check_arg_num():
    if not len(sys.argv) == 3:
        print("wrong number of inputs")
        sys.exit(1)

def check_image_input(input, output):
    input_lower = str(input).lower()
    output_lower = str(output).lower()

    if input_lower.endswith(".jpg"):
        type = ".jpg"
    elif input_lower.endswith(".jpeg"):
        type = ".jpeg"
    elif input_lower.endswith(".png"):
        type = ".png"
    else:
        print("File type wrong")
        sys.exit(1)

    if output_lower.endswith(type):
        pass
    else:
        print("File types do not match")
        sys.exit(1)

    if not os.path.exists(input):
        print("Input file does not exist")
        sys.exit(1)
    else:
        pass



def wear_tshirt(input, output):
    with Image.open("shirt.png") as shirt, Image.open(input) as img:
        dimensions = shirt.size
        fitted_img = ImageOps.fit(img, size=dimensions)
        fitted_img.paste(shirt, (0, 0), shirt)
        fitted_img.save(output)

main()
