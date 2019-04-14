from urllib.request import Request, urlopen
from json import loads
import ssl

certsPath='/usr/local/lib/python3.7/site-packages/pip/_vendor/certifi/cacert.pem'
context=ssl.SSLContext()
context.load_verify_locations(certsPath)

# Which character has the most associated films? When was the first and last of their films released?

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
            top_character.clear()
            top_character[list(people.keys())[i]] = people[key]
        i = i + 1

counter = 0
top_film = {}


def get_films():
    global key, counter
    for key in results:
        if key['name'] == str(list(top_character.keys())[0]):
            # print(key['films'])
            top_film[key['name']] = key['films']
        counter = counter + 1

get_most_associated_character()
get_films()

def clean_film_list():
    return str(list(top_film.values())[0]).replace('"', '').replace('[', '').replace(']', '').replace("'", "").split(
        ",")

film_list = clean_film_list()
first_film_date = '2030-01-01'
first_film_title = ''
last_film_date = '1900-01-01'
last_film_title = ''


def first_and_last_films():
    global key, url, results, first_film_date, first_film_title, last_film_date, last_film_title
    for key in film_list:
        url = str(key)
        results = []
        req = Request(url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req, context=context).read().decode("utf-8"))
        if data['release_date'] < first_film_date:
            first_film_date = data['release_date']
            first_film_title = data['title']
        if data['release_date'] > last_film_date:
            last_film_date = data['release_date']
            last_film_title = data['title']
        results += data


first_and_last_films()
print("Top Character: " + str(top_character))
print("First Film Title: " + first_film_title + " Date: " + first_film_date)
print("Last Film Title: " + last_film_title + " Date: " + last_film_date)


