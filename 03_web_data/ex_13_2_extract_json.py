import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter URL :')
uh = urllib.request.urlopen(url)
data = uh.read().decode()

info = json.loads(data)
comments = info['comments']
print('Counts:', len(comments))

total = 0
for comment in comments:
    total += comment['count']
print('Sum:' ,total)