# Scenario
# Create a Python module to check is the localhost already configured and whether the computer can access internet.

#!/usr/bin/env python3
import requests
import socket

def check_localhost():
  localhost = socket.gethostbyname('localhost')
  if localhost == '127.0.0.1':
    return True
  
def check_connectivity():
  request = requests.get("http://www.google.com")
  response = request.status_code
  if response == 200:
    return True
