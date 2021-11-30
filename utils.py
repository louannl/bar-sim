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

def set_user_character():
    player_options = {
        1: {'name': 'Buffy',
            'id': 140},
        2: {'name': 'Deadpool',
            'id': 213},
        3: {'name': 'Mystique',
            'id': 480},
        4: {'name': 'Rambo',
            'id': 540}
        }

    player_select = int(input(f"Which player would you like to select? Enter: \n1 for Buffy\n2 for Deadpool\n3 for Mystique\n4 for Rambo \nEnter your selection now: "))
    if player_select not in [1,2,3,4]:
        print("Oh dear, that is not one of our options. Let's try again.\n")
        set_user_character()
    selection=player_options[player_select]["name"]
    correct_selection = input(f"Is {selection} who you wish to play? y/n: ")
    while correct_selection == "n":
        for option in player_options.values():
            correct_selection = input(f"Is {option['name']} who you wish to play? y/n: ")
            if correct_selection == "y":
                return correct_selection
        return correct_selection #HOW DO I RETURN CORRECT_SELECTION TO CONT BELOW?
    if correct_selection == "y":
        id=player_options[player_select]["id"]
        print(id)

set_user_character()