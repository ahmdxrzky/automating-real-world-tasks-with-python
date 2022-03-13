#!/usr/bin/env python3
# This script is used for uploading all descriptions provided by supplier

# Import some external libraries
import os
import requests
import re
import json
import subprocess

# Change working dir to directory that contains description files
os.chdir('supplier-data/descriptions')
display = []

# Iterate through each file
for file in os.listdir():
  # Use try-except procedure to ensure only .txt file is being processed
  try:
    re.search(r"(.txt)$", os.path.abspath(file))
    if re.search(r"(.txt)$", os.path.abspath(file)) != None:
      # Read each of lines and store each line as value of different key from a dictionary and save it on a list
      with open(os.path.abspath(file), 'r') as txt_file:
        lines = txt_file.readlines()
        display_dict = {}
        display_dict["name"] = lines[0].strip()
        display_dict["weight"] = int(re.sub(r" lbs", "", lines[1].strip()))
        display_dict["description"] = lines[2].strip()
        display_dict["image_name"] = re.sub(r".txt", ".jpeg", file)
        display.append(display_dict)
  except IsADirectoryError:
    pass

# Create a JSON file of descriptions
with open('/home/{}/display.json'.format(os.environ.get('USER')), 'w') as json_file:
  json.dump(display, json_file, indent = 2)

# Write a response to ensure that code script executed properly
print("JSON file have been generated.")

sum_of_component = 0
sum_of_uploaded_desc = 0
for component in display:
  sum_of_component += 1
  # Upload descriptions one by one by iterating through each component of the list
  response = requests.post('http://104.154.156.54/fruits/', data = component)
  # Ensure that the description is uploaded successfully
  if response.status_code == 201:
    sum_of_uploaded_desc += 1

# Write a response to ensure that code script executed properly
print("{}/{} descriptions have been uploaded successfully.".format(sum_of_uploaded_desc, sum_of_component))
