import requests
from pprint import pprint

import random

def random_insult():
     url="https://evilinsult.com/generate_insult.php?lang=en&type=json"
     request = requests.get(url)
     request = request.json()
     print(request['insult'])

random_insult()

#To run rand_character() you need to go to https://superheroapi.com/ and get an access token. Put that into the access_token Variable e.g.

def rand_character():
     rand_gen=str(random.randint(1,731))
     access_token="YOUR GENERATED ACCESS CODE GOES HERE"
     url="https://superheroapi.com/api/"+ access_token + "/" + rand_gen
     request = requests.get(url)
     request = request.json()
     pprint(request)

rand_character()
