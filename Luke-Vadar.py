from urllib.request import Request, urlopen
from json import loads
import ssl

certsPath='/usr/local/lib/python3.7/site-packages/pip/_vendor/certifi/cacert.pem'
context=ssl.SSLContext()
context.load_verify_locations(certsPath)

# How many distinct starships are associated with Darth Vadar and Luke Skywalker?

url = 'https://swapi.co/api/people'
results = []
while url != None:
    req = Request(url, None, {
        'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
    })
    data = loads(urlopen(req, context=context).read().decode("utf-8"))
    results += data['results']
    url = data['next']
people = {}

for key in results:
    if key['name'] == 'Luke Skywalker' or key['name'] == 'Darth Vader':
        people[key['name']] = len(key['starships'])
print("Total Films : " + str(sum(people.values())))
