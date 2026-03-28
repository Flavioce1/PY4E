# PY4E - Using Python to Access Web Data
# Assignment: Scraping Numbers from HTML using BeautifulSoup
# Read an HTML page, extract all numbers from span tags and compute their sum.

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter URL: ")
if len(url) < 1:
    url = "http://py4e.com/code3/comments_42.html"

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("span")
total = 0
count = 0
for tag in tags:
    num = int(tag.string)
    total = total + num
    count = count + 1

print("Count:", count)
print("Sum:", total)
