# Scenario
# Your company is in the process of updating its website, and they've hired a design contractor to create some new icon graphics for the site.
# But the contractor has delivered the final designs in the wrong format -- rotated 90° clockwise and too large.
# Oof! You're not able to get in contact with the designers and your own deadline is approaching fast.
# You'll need to use Python to get these images ready for launch.

#!/usr/bin/env python3
# Import few external libraries
import PIL
from PIL import Image
import os
import re
import subprocess

# Change working dir to the directory contains pictures for manipulation process
os.chdir("images")

# Iterate through each file in the directory
sum_of_picture = 0
sum_of_manipulated_picture = 0
for picture_file in os.listdir():
  # Use try-except scenario to ensure the file is an image
  # If the file is not an image, an error of UnidentifiedImageError will be raised and the file will be passed
  try:
    picture = Image.open(picture_file)
    sum_of_picture += 1
    converted_picture = picture.convert('RGB')

    # Replace format of the file (delete .tiff part and replaced it with some customized name in format .jpeg)
    name = re.sub(r"(.tiff)$", "", picture_file)
    new_name = name + "_rotated_and_resized.jpeg"

    # Check if the file has been manipulated
    # If no, rotate, resize, and save with a new name in certain directory
    if re.search("_rotated_and_resized.jpeg", picture_file) == None:
      converted_picture.rotate(-90).resize((128,128)).save(new_name)
      old_place = os.path.abspath(new_name)
      new_place = "/opt/icons/" + new_name
      subprocess.run(["mv", old_place, new_place])
      sum_of_manipulated_picture += 1

  except PIL.UnidentifiedImageError:
    pass

# Write a response to ensure that script executed properly
print("{}/{} pictures has been manipulated successfully.".format(sum_of_manipulated_picture, sum_of_picture))
