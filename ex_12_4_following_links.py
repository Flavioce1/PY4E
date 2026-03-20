# PY4E - Using Python to Access Web Data
# Assignment: Following Links in HTML Using BeautifulSoup
# Start at a URL, find a link at a given position, follow it, repeat n times.

import urllib.request
from bs4 import BeautifulSoup

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    # grab the link at the right position (1-based)
    url = tags[position - 1].get("href")

print("Retrieving:", url)
