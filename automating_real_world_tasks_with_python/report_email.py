#!/usr/bin/env python3
# This script used for generate a customized PDF file and send it via email

# Import some external libraries
import os
import datetime
import sys
import json
import reports
import emails

def load_data(data):
  """Load a JSON file and return it as list of dictionaries."""
  with open(data) as json_file:
    data = json.load(json_file)
  return data

def main(argv):
  """Process the JSON data, generate a report out of it, and send it via email."""
  data = load_data("display.json")
  today_ = str(datetime.datetime.now())[:10]
  reports.generate_report("/tmp/processed.pdf", "Processed Update on {}".format(today_), data)

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully.\nA detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)
