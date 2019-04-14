from urllib.request import Request, urlopen
from json import loads
import ssl

# What is the fastest land vehicle?

certsPath='/usr/local/lib/python3.7/site-packages/pip/_vendor/certifi/cacert.pem'
context=ssl.SSLContext()
context.load_verify_locations(certsPath)

url = 'http://swapi.co/api/vehicles'
results = []
while url != None:
    req = Request(url, None, {
        'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
    })
    data = loads(urlopen(req, context=context).read().decode("utf-8"))
    results += data['results']
    url = data['next']
vehicles = {}
for key in results:
    if key['max_atmosphering_speed'] != 'unknown':
        vehicles[key['name']] = key['max_atmosphering_speed']
print(max(vehicles, key=lambda i: int(vehicles[i])))

