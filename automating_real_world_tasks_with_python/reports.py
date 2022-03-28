#!/usr/bin/env python3
# This script used for generate a PDF report file

# Import some external libraries
import json
import locale
import sys
import os

def generate_report(filename, title, data):
  """Generate a pdf file."""
  from reportlab.platypus import SimpleDocTemplate
  from reportlab.platypus import Paragraph, Spacer, Table, Image
  from reportlab.lib.styles import getSampleStyleSheet
  from reportlab.lib import colors

  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  empty_line = Spacer(1,20)
  report_content = [report_title, empty_line]

  # Data comes as list of dictionary
  for component in data:
    # Retrieve name and weight from each object
    additional_info = "name: " + component['name'] + '<br/>' + "weight: " + str(component['weight']) + " lbs"
    line = Paragraph(additional_info, styles["BodyText"])
    report_content.append(line)
    report_content.append(empty_line)

  report.build(report_content)
  # Write a response to ensure that code script executed properly
  print("Report has been generated as {}".format(filename))
