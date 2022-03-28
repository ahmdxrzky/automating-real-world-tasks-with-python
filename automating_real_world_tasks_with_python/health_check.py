#!/usr/bin/env python3
# This script used for checking machine's health

# Import some external libraries
import shutil
import psutil
import socket
import os
import sys
import emails

def check_cpu_usage():
  """Check if percentage of CPU usage is more than 80%."""
  cpu_usage_percent = psutil.cpu_percent(1)
  return cpu_usage_percent > 80

def check_disk_usage():
  """Check if percentage of available disk is lower than 20%."""
  available_disk_percent = (shutil.disk_usage("/").free / shutil.disk_usage("/").total) * 100
  return available_disk_percent < 20

def check_memory_usage():
  """Check if memory available is lower than 500 MB."""
  available_memory_in_MB = psutil.virtual_memory().available / (1024*1024)
  return available_memory_in_MB < 500

def check_resolve_hostname():
  """Check if the hostname resolved is not 127.0.0.1."""
  hostname = socket.gethostbyname('localhost')
  return hostname != '127.0.0.1'

def main(argv):
  """Check machine's health and send an email if an error occured."""
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  body = "Please check your system and resolve the issue as soon as possible."

  if check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)
  elif check_disk_usage():
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)
  elif check_memory_usage():
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)
  elif check_resolve_hostname():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)
  else:
    print("System on a well condition.")

if __name__ == "__main__":
  main(sys.argv)
