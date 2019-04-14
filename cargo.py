from urllib.request import Request, urlopen
from json import loads
import ssl

certsPath='/usr/local/lib/python3.7/site-packages/pip/_vendor/certifi/cacert.pem'
context=ssl.SSLContext()
context.load_verify_locations(certsPath)

# List all of the flying vehicles sorted by cargo capacity in ascending order?

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
vehicles2 ={}
for key in results:
    if key['cargo_capacity'] == 'unknown' or key['cargo_capacity'] == 'none':
        vehicles2[key['name']] = key['cargo_capacity']
    else:
        vehicles[key['name']] = key['cargo_capacity']
vehicles = sorted(vehicles.items(), key=lambda x: int(x[1]))
all_vehicles = vehicles.copy()
all_vehicles.append(vehicles2)

print(all_vehicles)

