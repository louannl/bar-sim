import os
from dotenv import load_dotenv

import requests
import random

load_dotenv()


def random_insult():
    return requests \
        .get("https://evilinsult.com/generate_insult.php?lang=en&type=json") \
        .json()['insult']


def rand_character():
    rand_gen = random.randint(1, 731)
    access_token = os.getenv('SUPERHERO_API_KEY')
    return requests.get(f"https://superheroapi.com/api/{access_token}/{rand_gen}").json()
