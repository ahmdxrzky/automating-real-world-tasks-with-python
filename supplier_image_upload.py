#!/usr/bin/env python3
# This script is used for uploading all of manipulated pictures (pictures with format .jpeg)

# Import some external libraries
import requests
import os
import re

url = "http://localhost/upload/"
# Change working dir to directory that contains manipulated pictures
os.chdir("supplier-data/images")

sum_of_picture = 0
sum_of_uploaded_picture = 0
# Iterate through each file
for pic in os.listdir():
  # Use regex to ensure only .jpeg picture are being processed
  if re.search("(.jpeg)", pic) != None:
    sum_of_picture += 1
    with open(os.path.abspath(pic), 'rb') as opened:
      r = requests.post(url, files={'file': opened})
      # Ensure if the picture are being uploaded
      if r.status_code == 201:
        sum_of_uploaded_picture += 1

# Write a response to ensure that code script executed properly
print("{}/{} pictures have been uploaded successfully.".format(sum_of_uploaded_picture, sum_of_picture))
