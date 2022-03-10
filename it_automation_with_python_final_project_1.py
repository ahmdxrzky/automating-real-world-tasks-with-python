# Scenario
# Your company is in the process of updating its website, and they've hired a design contractor to create some new icon graphics for the site.
# But the contractor has delivered the final designs in the wrong format -- rotated 90° and too large
# Oof! You're not able to get in contact with the designers and your own deadline is approaching fast.
# You'll need to use Python to get these images ready for launch.

# What I've done?
# Import some external libraries
# Move current working directory to folder that contains target files
# Iterate through each file
# Use try-except method to ensure only image file being opened
# Use regex to ensure format change procedure only not done to manipulated file
# Manipulate image file with rotate, resize, and rename it
# Move the file to a target folder

#!/usr/bin/env python3
import PIL
from PIL import Image
import os
import re
import subprocess

os.chdir("images")

for pic in os.listdir():
  # Check is the file is a image file
  # If yes, open the file
  try:
    im = Image.open(pic)
    new_pic = im.convert('RGB')

    # Replace format of the file
    name = re.sub(r"(.tiff)$", "", pic)
    new_name = name + "_rotated_and_resized.jpeg"

    # Check is the file has been manipulated
    # If no, rotate, resize, and save with a new name in certain directory
    if re.search("_rotated_and_resized.jpeg", pic) == None:
      new_pic.rotate(-90).resize((128,128)).save(new_name)
      old_place = os.path.abspath(new_name)
      new_place = "/opt/icons/"+ new_name
      subprocess.run(["mv", old_place, new_place])

  except PIL.UnidentifiedImageError:
    pass
