import sys
import os
from PIL import Image


# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create it

if os.path.isdir(output_folder) == False:
    os.mkdir(output_folder)

# loop through Pokedex
for filename in os.listdir(image_folder):
    img = Image.open("{}/{}".format(image_folder, filename))
    # this command splits the name and format and returns a tuple
    clean_name = os.path.splitext(filename)[0]
    img.save("{}/{}.png".format(output_folder, clean_name), "png")
