import os
from dotenv import load_dotenv
import requests
import random

load_dotenv()


def random_insult():
    url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    try:
        request = requests.get(url).json()
        return request['insult']
    except requests.exceptions.ConnectionError:
        print(f"Unable to connect to api {url}.")


def get_random_beer():
    beers = ['Stella Artois', 'Peroni', 'Heineken', 'Magners']
    return random.choice(beers)


def get_character(num):
    access_token = os.getenv('SUPERHERO_API_KEY')
    url = f"https://superheroapi.com/api/{access_token}/{num}"
    try:
        return requests.get(url).json()
    except requests.exceptions.ConnectionError:
        print(f"Unable to connect to api {url}.")


def get_random_superhero():
    superhero_list = {
        60: "Bane",
        69: "Batman",
        97: "Black Canary",
        309: "Harlequin",
        322: "Hellboy",
        522: "Poison Ivy",
        374: "Juggernaut",
        400: "Lady Deathstrike",
        489: "Nick Fury"
    }
    return random.choice(list(superhero_list.keys()))


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


def main_character_get_character(player_options):
    print("Which player would you like to select? Alternatively, enter 'q' to quit")
    player_key_index = 0
    player_name_index = 0
    for player_option in range(len(player_options)):
        print(list(player_options.keys())[player_key_index], "...",
              list(player_options.items())[player_name_index][1]["name"])
        player_key_index += 1
        player_name_index += 1


def user_selection():
    user_select = input("Enter the id number for the character you would like to select now: ")
    return user_select


def main_character_selection(user_select):
    # Would decorators somehow be helpful to us?
    if user_select == "q":
        print("Thank you for playing Get Served.")
        exit()
    try:
        if player_options[int(user_select)]:
            print(player_options[int(user_select)]["name"])  # LINE FOR TESTING ONLY
            print(player_options[int(user_select)]["id"])  # LINE FOR TESTING ONLY
            return player_options[int(user_select)]["id"]
    except ValueError as err:  # not raising this properly - type i as input you will see what I mean. Also want to raise a KeyValue error without having to repeat code below?
        print(
            f"{err}: I'm sorry that is not a recognised option. Please enter the character id number you wish to select, e.g. '2'. Let's try again.\n")
        main_character_get_character(player_options)
        main_character_selection(user_selection())
        raise


# EXAMPLE CALLS
main_character_get_character(player_options)
main_character_selection(user_selection())
