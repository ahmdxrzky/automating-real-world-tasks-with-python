#!/usr/bin/env python3
# This script is used for resizing and changing format of all .tiff picture to .jpeg format

# Import some external libraries
import PIL
from PIL import Image
import os
import re

# Change working dir to directory that contains manipulation target pictures
os.chdir("supplier-data/images")

sum_of_picture = 0
sum_of_manipulated_picture = 0
# Iterate through each file
for pic in os.listdir():
  # Use try-except procedure to ensure only image file being opened
  try:
    im = Image.open(pic)
    new_pic = im.convert('RGB')

    # Replace format of the file
    if re.search(r"(.tiff)$", pic) != None:
      name = re.sub(r"(.tiff)$", "", pic)
      new_name = name + ".jpeg"
      sum_of_picture += 1

    # Check is the image already being manipulated
    # If no, resize it
    if re.search(r".jpeg", pic) == None:
      new_pic.resize((600,400)).save(new_name)
      sum_of_manipulated_picture += 1

  except IsADirectoryError:
    pass

  except PIL.UnidentifiedImageError:
    pass

# Write a response to ensure that code script executed properly
print("{}/{} pictures has been manipulated successfully.".format(sum_of_manipulated_picture, sum_of_picture))
