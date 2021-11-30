import os
from dotenv import load_dotenv

import requests

def random_insult():
     try:
          url="https://evilinsult.com/generate_insult.php?lang=en&type=json"
          request = requests.get(url)
     except:
          raise ConnectionError(f"Unable to connect to api {url}.")
     else:
          request = request.json()
          return(request['insult'])

load_dotenv()

def get_character(num):
    access_token = os.getenv('SUPERHERO_API_KEY')
    url = (f"https://superheroapi.com/api/{access_token}/{num}")
    try:
        request = requests.get(url)
    except:
        raise ConnectionError(f"Unable to connect to api {url}.")
    else:
        request = request.json()
        return (request)
