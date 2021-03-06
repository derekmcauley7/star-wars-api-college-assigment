from urllib.request import Request, urlopen
from json import loads
import ssl

# How many people are returned by the API? Show how you can solve this without using the results count attribute?s

certsPath='/usr/local/lib/python3.7/site-packages/pip/_vendor/certifi/cacert.pem'
context=ssl.SSLContext()
context.load_verify_locations(certsPath)

url = 'http://swapi.co/api/people'
results = []
while url != None:
    req = Request(url, None, {
        'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
    })
    data = loads(urlopen(req, context=context).read().decode("utf-8"))
    results += data['results']
    url = data['next']

print("Number of people: " + str(len(results)))