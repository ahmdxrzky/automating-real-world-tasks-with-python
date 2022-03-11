# Scenario
# You're working at a company that sells second-hand cars. Your company constantly collects feedback in the form of customer reviews.
# Your manager asks you to take those reviews (saved as .txt files) and display them on your company's website.
# To do this, you'll need to write a script to convert those .txt files and process them into Python dictionaries,
# then upload the data onto your company's website (currently using Django).

# What I've done?
# Import some external libraries __ (1)
# Move working directory to folder that contains feedback files __ (2)
# Iterate through each feedback files __ (3)
# Use try-except and regex to ensure that only txt files being processed __ (4)
# Read each lines on the a file and add those lines as a dictionary __ (5)
# Join all dictionaries to a list __ (6)
# Iterate through each components on the list and post it to web one by one ___ (7)

#!/usr/bin/env python3
# (1)
import os
import requests
import re

# (2)
os.chdir('/data/feedback')
display = []

# (3)
for file in os.listdir():
  try:
    # (4)
    re.search(r"(.txt)$", os.path.abspath(file))
    if re.search(r"(.txt)$", os.path.abspath(file)) != None:
      # (5)
      with open(os.path.abspath(file), 'r') as txt_file:
        lines = txt_file.readlines()
        display_dict = {}
        display_dict['title'] = lines[0].strip()
        display_dict['name'] = lines[1].strip()
        display_dict['date'] = lines[2].strip()
        display_dict['feedback'] = lines[3].strip()
        # (6)
        display.append(display_dict)
  except IsADirectoryError:
    pass

# (7)
for component in display:
  response = requests.post('http://34.70.131.158/feedback/', data = component)
  print(response.status_code)
