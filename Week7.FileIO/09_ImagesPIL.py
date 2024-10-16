# We've just handled text files
# But other files are binary files
# PIL or Pillow is an image handler
# pillow.readthedocs.io

# We want to create an animated gif.

# Now I don't have the required files
# But imagine I had costume1.gif and costume2.gif and wanted to alternate them

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:    # Take the slice omitting the first thing, which is the name of the program we provide
# So I want to run this file, supply 2 image files as arguments and pass to Image.open function
    image = Image.open(arg)
    images.append(image) # Put the 2 images into the images list

images[0].save(     # save the image with another image appended to it to make it a gif
    "costumes.gif", save_all=True, append_images=images[1], duration=200, loop=0
)
