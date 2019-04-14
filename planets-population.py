from urllib.request import Request, urlopen
from json import loads
import ssl

certsPath='/usr/local/lib/python3.7/site-packages/pip/_vendor/certifi/cacert.pem'
context=ssl.SSLContext()
context.load_verify_locations(certsPath)

# List the names of all planets sorted by (one list each)
# diameter in ascending order
# population in descending order
#

url = 'https://swapi.co/api/planets'


def api_request():
    global results, url
    results = []
    while url != None:
        req = Request(url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req, context=context).read().decode("utf-8"))
        results += data['results']
        url = data['next']


api_request()

def separate_planets_with_and_without_populations():
    global planets_with_polulation, planets_without_polulation
    planets_with_polulation = {}
    planets_without_polulation = {}
    for key in results:
        if key['population'] == 'unknown':
            planets_without_polulation[key['name']] = key['population']
        else:
            planets_with_polulation[key['name']] = key['population']


separate_planets_with_and_without_populations()

planets_with_polulation = sorted(planets_with_polulation.items(), key=lambda x: int(x[1]), reverse=True)

def rejoin_planet_lists():
    global all_planets_in_order
    all_planets_in_order = planets_with_polulation.copy()
    all_planets_in_order.append(planets_without_polulation)


rejoin_planet_lists()
print(all_planets_in_order)
