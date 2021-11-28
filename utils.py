import requests

import random

def random_insult():
     try:
          url="https://evilinsult.com/generate_insult.php?lang=en&type=json"
          request = requests.get(url)
     except:
          raise ConnectionError(f"Unable to connect to api {url}.")
     else:
          request = request.json()
          return(request['insult'])



#To run rand_character() you need to go to https://superheroapi.com/ and get an access token. Put that into the access_token Variable e.g.
#The below code calls the full json for the random superhero selected

def rand_character():
     rand_gen=str(random.randint(1,731))
     access_token="YOUR GENERATED ACCESS CODE GOES HERE"
     url=(f"https://superheroapi.com/api/{access_token}/{rand_gen}")
     try:
          request = requests.get(url)
     except:
          raise ConnectionError(f"Unable to connect to api {url}.")
     else:
          request = request.json()
          return(request)

if __name__ == '__main__':
     random_insult()
     rand_character()
