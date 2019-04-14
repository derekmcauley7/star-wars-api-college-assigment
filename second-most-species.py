from urllib.request import Request, urlopen
from json import loads
import ssl

certsPath='/usr/local/lib/python3.7/site-packages/pip/_vendor/certifi/cacert.pem'
context=ssl.SSLContext()
context.load_verify_locations(certsPath)

# What species appears the second-most often in a film?

def make_api_request(url):
    global results
    results = []
    while url != None:
        req = Request(url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req, context=context).read().decode("utf-8"))
        results += data['results']
        url = data['next']

url = 'https://swapi.co/api/people'
make_api_request(url)

def character_with_number_of_films():
    global people, key
    people = {}
    for key in results:
        people[key['name']] = len(key['films'])

character_with_number_of_films()

top_character = {}
top = 0
i = 0

def get_most_associated_character():
    global key, top, i
    for key in people:
        if (people[key] >= top):
            top = people[key]
            top_character[list(people.keys())[i]] = people[key]
        i = i + 1
    print("Top character list: " + str(top_character))

get_most_associated_character()

second_most_character = str(sorted(top_character.keys())[0])
species_url = ''
species = ''
print("Character that appears the second-most often in a film : " + str(second_most_character))
for key in results:
    new_results =  []
    if key['name'] == second_most_character:
        species_url=key['species'][0]
        results = []
        req = Request(species_url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req, context=context).read().decode("utf-8"))
        species = data['classification']
        results += data

print("Species that appears the second-most often in a film :  " + str(species))
