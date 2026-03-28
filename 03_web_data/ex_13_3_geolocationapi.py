import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter location: ')
url = 'http://py4e-data.dr-chuck.net/opengeo?' + urllib.parse.urlencode({'q': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
plus_code = info['features'][0]['properties']['plus_code']
print('Plus code', plus_code)