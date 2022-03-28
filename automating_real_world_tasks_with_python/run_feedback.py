# Scenario
# You're working at a company that sells second-hand cars. Your company constantly collects feedback in the form of customer reviews.
# Your manager asks you to take those reviews (saved as .txt files) and display them on your company's website.
# To do this, you'll need to write a script to convert those .txt files and process them into Python dictionaries,
# then upload the data onto your company's website (currently using Django).

#!/usr/bin/env python3
# Import some external libraries
import os
import requests
import re

# Change working dir to the directory contains feedback from users
os.chdir('/data/feedback')

# Define a list as a place for storing feedbacks from files
display = []

# Iterate through each file
sum_of_txt = 0
sum_of_feedback = 0
for file in os.listdir():
  # Use try-except procedure and regex to ensure that only a txt file is being opened
  try:
    if re.search(r"(.txt)$", os.path.abspath(file)) != None:
      with open(os.path.abspath(file), 'r') as txt_file:
        sum_of_txt += 1
        lines = txt_file.readlines()
        display_dict = {}
        display_dict['title'] = lines[0].strip()
        display_dict['name'] = lines[1].strip()
        display_dict['date'] = lines[2].strip()
        display_dict['feedback'] = lines[3].strip()
        display.append(display_dict)
        sum_of_feedback += 1
  except IsADirectoryError:
    pass

# Iterate through each feedback and post it to the web service
success_status_code = 0
for component in display:
  response = requests.post('http://35.238.177.139/feedback/', data = component)
  if response.status_code == 201:
    success_status_code += 1

# Write a response to ensure that code script executed properly
print("{} feedbacks from {}/{} files has been uploaded successfully.".format(success_status_code, sum_of_feedback, sum_of_txt))
