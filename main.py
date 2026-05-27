# Import the requests library so we can send HTTP requests to websites
import requests

# Import BeautifulSoup so we can parse and search through HTML later
from bs4 import BeautifulSoup

# Store the website URL we want to request
url = "https://www.livescore.com/en/"

# Send a GET request to the website and store the response
response = requests.get(url)

# Get the HTTP status code from the response
status = response.status_code

# Print the status code to the terminal
print(status)
