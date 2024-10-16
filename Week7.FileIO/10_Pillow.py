# Pillow is for manipulating images in python

# I have a file called wave.jpeg
# It is upside down though.
# Let's use the Pillow Library to flip it

# I need access to a 'class' inside of PIL called Image
# A class is a bit like a template, some way of representing information
# more on classes later on

from PIL import Image
from PIL import ImageFilter

def main():
    # We open it and refer to the image object by naming it as a variable img
    # and it will close afterwards
    with Image.open("wave.jpg") as img:
        # width by height
        print(img.size)
        # file type
        print(img.format)
        # Manipulating the image, he taught me to do img = image.rotate(180)
        # But that didn't work.
        # This Version does seem to work.
        img.rotate(180)
        img.save("wave_flip.jpg")

    # New manipulation: blur filter
    with Image.open("wave.jpg") as img:
        img = img.filter(ImageFilter.BLUR)
        img.save("wave_blur.jpg")

    # New manipulation: highlight edges
    with Image.open("wave.jpg") as img:
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("wave_edges.jpg")


main()
