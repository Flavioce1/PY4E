# PY4E - Using Python to Access Web Data
# Assignment: Extracting Data from XML
# Read XML from a URL, find all count tags and compute the sum.

import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter URL: ")
if len(url) < 1:
    url = "http://py4e.com/code3/comments_42.xml"

data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)

counts = tree.findall(".//count")

total = 0
for count in counts:
    total = total + int(count.text)

print("Count:", len(counts))
print("Sum:", total)
